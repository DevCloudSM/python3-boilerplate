import views
from flask import Flask

class Application: 
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/ping', view_func=views.ping)

    def run(self):
        self.app.run(debug=True, use_reloader=True)

app = Application()

# For wsgi (two arguments are required)
def start(environ, start_response):
    return app.app(environ, start_response)
    
if __name__ == '__main__':
    start()