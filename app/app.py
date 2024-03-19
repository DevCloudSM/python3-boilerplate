import views
import os
import logging 
from flask import Flask
from database import db

if (os.getenv("DEBUG", "TRUE") == "TRUE"): 
    logging.basicConfig(level = logging.DEBUG)
    
class Application: 
    def __init__(self):
        self.app = Flask(__name__)
        
        db_c = {
            "host": os.getenv("DB_HOST", "localhost"),
            "user": os.getenv("DB_USER", "postgres"),
            "pass": os.getenv("DB_PASSWORD", "bonjour"),
            "name": os.getenv("DB_PROJECT", "project"),
            "port": os.getenv("DB_PORT", "5432")
        }
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_c['user']}:{db_c['pass']}@{db_c['host']}:{db_c['port']}/{db_c['name']}"
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['DEBUG'] = (os.getenv("DEBUG", "TRUE") == "TRUE")
        db.init_app(self.app)
        
        # DB check if all tables are created
        if os.getenv("DB_CREATE", "FALSE") == "TRUE":
            with self.app.app_context():
                print("Creating all tables")
                #db.delete_all()
                db.create_all()

        self.init_routes()
        
    def run(self):
        self.app.run(debug=(os.getenv("DEBUG", "TRUE") == "TRUE"), use_reloader=True)

    def init_routes(self):
        self.app.add_url_rule('/ping', view_func=views.ping, methods=['GET'])
        self.app.add_url_rule('/testDB', view_func=views.testDB, methods=['GET'])
app = Application()

# For wsgi (two arguments are required)
def start(environ, start_response):
    return app.app(environ, start_response)
    
if __name__ == '__main__':
    start()