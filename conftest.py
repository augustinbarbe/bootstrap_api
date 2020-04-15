import pytest
from flask import Flask
from bootstrap import init_app
from bootstrap import db


@pytest.fixture(autouse=True)
def app():
    app = Flask(__name__)

    with app.app_context():
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        init_app(app)
        db.drop_all()
        db.create_all()

    client = app.test_client()
    yield client


