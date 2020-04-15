from flask_restplus import Api, fields
from bootstrap.apis.collection import api as ns_small
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    title='RESTFUL API',
    version='1.0',
    description='',
    authorizations=authorizations
)


api.namespaces.clear()
api.add_namespace(ns_small)
