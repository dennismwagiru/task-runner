import os
import subprocess
from bson.objectid import ObjectId

from celery import Celery

from src.app.db import db


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "redis://localhost:6379"
)
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379"
)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # run pending commands every 10 seconds.
    sender.add_periodic_task(10.0, run_commands.s(), name='add every 10')


@celery.task(name="run_commands")
def run_commands():
    for task in db.tasks.find({"status": "pending"}):
        command_id = task.get('_id')
        command = task.get('command')
        try:
            result = subprocess.check_output(
                [command], shell=True)
            task['output'] = ('%s' % result)
        except subprocess.CalledProcessError as e:
            task['output'] = "An error occurred: %s" % e.output
        task['status'] = "completed"
        db.tasks.replace_one({'_id': ObjectId(command_id)}, task)
