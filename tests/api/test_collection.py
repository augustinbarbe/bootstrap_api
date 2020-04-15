"""
Test here all the access points of the API for a given ressource
It is meant to leverage the entire code of the api
"""
import json


def test_app(app):
    res = app.get('/collections/')
    assert res.status_code == 200


def test_create(app):
    res = app.post('/collections/',
                   data=json.dumps(dict(field='TEST-VALUE')),
                   content_type='application/json')

    assert res.status_code == 200


def test_get(app):
    # GIVEN
    created = app.post('/collections/',
                       data=json.dumps(dict(field='TEST-VALUE')),
                       content_type='application/json')
    created_object_id = json.loads(created.data)["iid"]

    # WHEN
    res = app.get(f'/collections/{created_object_id}')

    # THEN
    assert res.status_code == 200
    assert json.loads(res.data)["field"] == 'TEST-VALUE'
