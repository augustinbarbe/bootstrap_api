from setuptools import setup

setup(
    name='API bootstrap',
    packages=['bootstrap'],
    include_package_data=False,
    install_requires=[
        'gunicorn',
        'flask_restplus',
        'flask_migrate',
        'flask_CORS',
        'flask_sqlalchemy',
        'Werkzeug==2.2.3'
    ],
)
