from flask import Flask
from flask_cors import CORS

from bootstrap.apis import api
from bootstrap.repositories.models import db


def load_configuration(app):
    """ Load application configuration from the api configuration python module"""
    app.config.from_pyfile('../config/api_conf.py')


def init_app(app):
    """Initialize extensions of flask"""
    api.init_app(app)
    db.init_app(app)
    # Change origins to adequate value for a more secure approach
    CORS(app, resources={r"/*": {"origins": "*"}})


def create_app():
    """Factory for flask application
    Entry point function for WSGI servers
    """
    app = Flask(__name__)
    load_configuration(app)
    init_app(app)

    return app


app = create_app()
