from flask import jsonify, Response

def ping() -> Response:
    """Retourne pong! pour tester la connexion au serveur

    Returns:
        json: {"message": "pong!"}
    """
    return jsonify({"message": "pong!"})
