from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
api = Api()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.resources import contacts_api
    app.register_blueprint(contacts_api)

    api.init_app(app)
    db.init_app(app)

    return app
