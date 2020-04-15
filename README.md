# GENERIC API BOOTSTRAP

This is my very own implementation of a RESTFUL API based on flask and flask-RESTPLUS

It includes the following capabilities :
- Swagger documentation
- SQL database operations
- asynchronous job processing

It comes with a pre-configured tox test runner, a Dockerfile with entrypoints for the API and the 
asynchronous workers and a buildspec.yml if you whish to store the build on AWS ECR.

The architecture revolves around the clean separation of the controllers, business layer 
and data-access/repository layer in order for the business to be completly agnostic of any technology used.
I chose to not implement a business layer for crud operations as it seems redundant with the repository : 
https://stackoverflow.com/questions/16211858/in-multi-layered-architecture-can-i-skip-the-business-layer-for-crud-operations


# TODO :

Core
- pagination
- asynchronous job follow-up
- authentication
- maybe a better way of serializing objects (Mashmallow) and avoid model definition redunduncy

Optional :
- add linter
- postman tests



## Development

```bash
git clone https://github.com/augustinbarbe/api_bootstrap
cd api_bootstrap/
```

Run tests with tox : 

```bash
pip install tox
tox
``` 

Run the API locally

```bash
source ./env
./scripts/run_dev.sh dev
```

You should be able to access to the documentation through http://localhost:5000/

