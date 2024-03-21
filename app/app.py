import views
import os
from flask import Flask
from database import db
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from utils import PathUtils
    
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
        self.sql_url = f"postgresql://{db_c['user']}:{db_c['pass']}@{db_c['host']}:{db_c['port']}/{db_c['name']}"
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.sql_url
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['DEBUG'] = (os.getenv("DEBUG", "TRUE") == "TRUE")

        self.pUtils = PathUtils()

        if not os.path.isfile(self.pUtils.getDataPath() / ".firstrun"):
            self.first_run()
        else :
            db.init_app(self.app)
        

        # DB check if all tables are created
        if os.getenv("DB_CREATE", "FALSE") == "TRUE":
            with self.app.app_context():
                print("Creating all tables")
                db.delete_all()
                db.create_all()

        self.init_routes()


    def first_run(self):
            print("############### RUNNING FIRST RUN SCRIPT ###############")
            engine = create_engine(self.sql_url)
            if not database_exists(engine.url):
                create_database(engine.url)
                print("> Database created")
            else :
                print("> Database already exists")
            db.init_app(self.app)
            print("> App started")
            with self.app.app_context():
                db.create_all()
            print("> Tables created")
            open(self.pUtils.getDataPath() / ".firstrun", 'w').close()
            print("> Status saved")

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