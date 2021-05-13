import os
import time

from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "redis://localhost:6379"
)
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379"
)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')


@celery.task(name="test_task")
def test(arg):
    print(arg)


@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
