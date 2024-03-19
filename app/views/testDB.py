from flask import jsonify, Response
from database import db
from models.users import Users

def testDB() -> Response:
    """Database Test 
    
    Returns:
        json: {"data": "..."}
    """
    # Add user to the database
    user = Users(username="test") 
    db.session.add(user)
    db.session.commit()
    # Get the user from the database
    test = Users.query.first().to_dict()
    return jsonify({"data": test})