import json
import os

from flask import Flask, jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

from src.app.config import app_config
from src.app.db import db


def create_app(environment=None):
    if environment is None:
        environment = os.environ.get("FLASK_ENV", 'development')
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[environment])

    @app.route("/")
    def index():
        return jsonify(
            status=True,
            message='Welcome to the Dockerized Flask MongoDB app!'
        )

    @app.route("/new_task", methods=['POST'])
    def new_task():
        _json = request.json
        _command = _json['command']
        if _command:
            _id = db.tasks.insert_one({'command': _command,
                                       'status': 'pending'}).inserted_id
            resp = jsonify(id=str(_id))
            resp.status_code = 201
            return resp

    @app.route('/tasks')
    def users():
        tasks = db.tasks.find()
        resp = jsonify(json.loads(dumps(tasks)))
        return resp

    @app.route('/get_output/<id>')
    def get_output(id):
        task = db.tasks.find_one({'_id': ObjectId(id)})
        if task:
            resp = jsonify(output=task.get('output'))
            resp.status_code = 200
        else:
            resp = jsonify('Not Found')
            resp.status_code = 404
        return resp

    return app
