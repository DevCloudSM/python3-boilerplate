from sqlalchemy_serializer import SerializerMixin
from database import db

class Users(db.Model, SerializerMixin):
    """Users Model
    
    Matches the Users table in the database
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=True)
    def __repr__(self):
        return f'<Users {self.id}>'
    