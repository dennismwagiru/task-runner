from unittest.mock import patch

from src.app.tasks import create_task


def test_task():
    assert create_task.run(1)
    assert create_task.run(2)
    assert create_task.run(3)


@patch("src.app.tasks.create_task.run")
def task_mock_task(self):
    assert create_task.run(1)
    create_task.run.assert_called_once_with(1)

    assert create_task.run(2)
    assert create_task.run.call_count == 2

    assert create_task.run(3)
    assert create_task.run.call_count == 3
