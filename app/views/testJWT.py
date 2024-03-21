from flask import jsonify, Response, request, abort, current_app
import jwt
from utils import PathUtils

def TestJWT() -> Response:
    if not current_app.debug:
       return abort(404)
    if request.cookies.get('token') is not None:
        token = request.cookies.get('token')
    else :
        try :
            authorization = request.headers['Authorization'].split(" ")
            if authorization[0] == "Bearer":
                token = authorization[1]
            else :
                return send_error("Invalid authentication method")
        except KeyError as e:
            return send_error("Please provide 'token' cookie OR username and password as HTTP basic auth header")

    pUtils = PathUtils()
    with open(pUtils.getSharedPath() / "jwt_rsa.pem", mode="rb") as pubkey:
        try:
            data = jwt.decode(token, pubkey.read(), algorithms="RS256")
        except jwt.exceptions.InvalidSignatureError:
            return send_error("Invalid signature")
        except jwt.exceptions.DecodeError:
            return send_error("Wrong token format")
        except jwt.ExpiredSignatureError:
            return send_error("Expired token")
        except jwt.exceptions.InvalidAlgorithmError:
            return send_error("Unexpected algorithm")
    return jsonify({"_WARNING": "This endpoint is only accessible in DEBUG MODE. Do not USE it IN PRODUCTION.", "status": "success", "data": data})

def send_error(message: str, code: int=400, debug: str="") -> tuple[str, int]:
    if debug != "":
        debug = " > "+debug
    print(message+debug)    
    return jsonify({"status": "error", "error_message": message}), code