from flask import Flask, jsonify
from flask_pymongo import PyMongo

from instance.config import app_config


def create_app(config_name):
    print(config_name)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    mongo = PyMongo(app)
    db = mongo.db

    @app.route("/")
    def index():
        return jsonify(
            status=True,
            message='Welcome to the Dockerized Flask MongoDB app!'
        )

    return app
