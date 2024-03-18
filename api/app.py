import views
from flask import Flask

class Application: 
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/ping', view_func=views.ping)

    def run(self):
        self.app.run(debug=True, use_reloader=True)

app = Application()

if __name__ == '__main__':
    app.run()