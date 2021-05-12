import os

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId

from app.config import app_config


def create_app():
    ENVIRONMENT = os.environ.get("FLASK_ENV", 'development')
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[ENVIRONMENT])
    mongo = PyMongo(app)
    db = mongo.db

    @app.route("/")
    def index():
        return jsonify(
            status=True,
            message='Welcome to the Dockerized Flask MongoDB app!'
        )

    @app.route("/new_task", methods=['POST'])
    def new_task():
        _json = request.json
        if 'command' in _json and _json['command']:
            _command = _json['command']
            command = db.tasks.insert({
                'command': _command, 'status': 'pending'
            })
            resp = dumps(command)
            return resp

    @app.route('/tasks')
    def users():
        tasks = db.tasks.find()
        resp = dumps(tasks)
        return resp

    @app.route('/get_output/<id>')
    def get_output(id):
        task = mongo.db.tasks.find_one({'_id': ObjectId(id)})
        resp = dumps(task)
        return resp

    @app.errorhandler(404)
    def not_found():
        message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404

        return resp

    return app
