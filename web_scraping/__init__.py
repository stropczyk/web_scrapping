from flask import Flask

from .main.routes import main
from .errors.handlers import errors


app = Flask(__name__)
app.config['SECRET_KEY'] = '8G3-Rr5qjsGE2dVuUI2wXw'
app.register_blueprint(main)
app.register_blueprint(errors)


def create_app():
    app = Flask(__name__)

    from web_scraping.main.routes import main
    app.register_blueprint(main)

    return app
