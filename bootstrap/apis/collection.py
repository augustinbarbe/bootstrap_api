# -*- coding: utf-8 -*-
"""API module.
This module contains all the controllers for a given route
It should only contains repository objects or business logic

Here we deal with syncrhonous operations
"""

from flask import request
from flask_restplus import Namespace, Resource, fields
from bootstrap.repositories.collection import ObjectRepository, ObjectNotFoundError

api = Namespace('collections', description='Operations for a given collection')

# API models
resource_write = api.model('ResourceWrite', {
    'field': fields.String
})

resource_read = api.clone('ResourceRead', resource_write, {
    'iid': fields.Integer,
    'created_on': fields.DateTime(),
    'updated_on': fields.DateTime(),
})


# Error handlere
@api.errorhandler(ObjectNotFoundError)
def handle_not_found():
    return {'message': 'The requested object does not exist'}, 400


@api.route('/')
class ResourceObjects(Resource):
    @api.marshal_list_with(resource_read, envelope='Objects')
    @api.doc(description='List all objects.')
    def get(self):
        return ObjectRepository.get_all()

    @api.expect(resource_write, validate=True)
    @api.marshal_with(resource_read)
    @api.doc(description='Create a new object')
    def post(self):
        payload = request.get_json()
        return ObjectRepository.create(payload)

@api.route('/<int:resource_id>')
@api.param('resource_id', 'The resource identifier')
@api.response(404, 'The requested object does not exist')
class ResourceObject(Resource):
    @api.marshal_with(resource_read)
    @api.doc(description='Get one collection.')
    def get(self, resource_id):
        return ObjectRepository.get(resource_id)

    @api.expect(resource_write, validate=True)
    @api.marshal_with(resource_read)
    @api.doc(description='Update an object')
    def put(self, resource_id):
        payload = request.get_json()
        ObjectRepository.edit(resource_id, payload)

    @api.doc(description='Delete an object given its id')
    def delete(self, resource_id):
        ObjectRepository.delete(resource_id)
        return 200
