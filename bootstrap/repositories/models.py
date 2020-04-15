# -*- coding: utf-8 -*-
"""SQLAlchemy models.
This module contains all the model definitions used by SQLAlchemy.
Those models should not be exposed directly in the business layer but through a repository layer
"""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SomeObject(db.Model):
    iid = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    field = db.Column(db.String)


class Job(db.Model):
    iid = db.Column(db.Integer, primary_key=True)
