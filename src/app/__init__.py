import json
import os
import subprocess

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId

from src.app.config import app_config
from src.app.tasks import create_task


def create_app(environment=None):
    if environment is None:
        environment = os.environ.get("FLASK_ENV", 'development')
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[environment])
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
        _command = _json['command']
        if _command:
            _id = db.tasks.insert({'command': _command, 'status': 'pending'})
            try:
                result = subprocess.check_output(
                    [_command], shell=True)
                resp = jsonify(id=str(_id), result='%s' % result)
                resp.status_code = 201
                return resp
            except subprocess.CalledProcessError as e:
                resp = jsonify(
                    id=str(_id),
                    message="An error occurred while processing your command"
                )
                resp.status_code = 400
                return resp

    @app.route('/tasks')
    def users():
        tasks = db.tasks.find()
        resp = dumps(tasks)
        return resp

    @app.route('/get_output/<id>')
    def get_output(id):
        task = mongo.db.tasks.find_one_or_404({'_id': ObjectId(id)})
        resp = jsonify(json.loads(dumps(task)))
        return resp

    @app.errorhandler(404)
    def not_found(e):
        message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404

        return resp

    return app
