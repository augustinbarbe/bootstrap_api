#!/usr/bin/env bash

pip install .

export FLASK_DEBUG="True"
export FLASK_APP="bootstrap:create_app()"
export SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db'
export API_SECRET_KEY='asecretkey'

flask run -h 0.0.0.0 -p 8000