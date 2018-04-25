from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy 
from instance.config import app_config
from app.models import User


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    api_manager = APIManager(app, flask_sqlalchemy_db=db)
    api_manager.create_api(
        User, 
        methods=['GET', 'POST', 'PUT', 'DELETE'],
        url_prefix='/api/v1',
    )

    # The routes will go here

    return app

