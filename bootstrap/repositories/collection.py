# -*- coding: utf-8 -*-
"""Repository layer.

This module contains the layer for accessing data in order to isolate the business layer and the controllers
out of any database access
"""

from bootstrap.repositories.models import SomeObject as SomeObjectModel, db


class ObjectRepository:
    @staticmethod
    def create(payload):
        resource = SomeObjectModel(**payload)
        db.session.add(resource)
        db.session.commit()
        return resource

    @staticmethod
    def get_all():
        return SomeObjectModel.query.all()

    @staticmethod
    def get(resource_id):
        some_object = SomeObjectModel.query.filter_by(iid=resource_id).one()
        if not some_object:
            raise ObjectNotFoundError()
        return some_object

    @staticmethod
    def delete(resource_id):
        object_to_delete = ObjectRepository.get(resource_id)
        db.session.delete(object_to_delete)
        db.session.commit()

    @staticmethod
    def edit(resource_id, payload):
        some_object = ObjectRepository.get(resource_id)
        for k, v in payload.items():
            setattr(some_object, k, v)
        db.session.commit()
        return some_object


def ObjectNotFoundError(Exception):
    pass
