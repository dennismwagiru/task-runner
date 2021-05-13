import json
import unittest

from src.app import create_app


class TaskRunnerApiTestCase(unittest.TestCase):
    """This class represents the api test case"""

    def setUp(self) -> None:
        """Define test variables and initialize app."""
        self.app = create_app(environment="testing")
        self.client = self.app.test_client
        self.task = {'command': 'ls'}

    def test_new_task_endpoint(self):
        """Test API can create a new task (POST request)"""
        res = self.client().post('/new_task', json=self.task)
        self.assertEqual(res.status_code, 201)
        self.assertIn('id', str(res.data))

    def test_list_tasks(self):
        """Test API can get a list of all tasks (GET request)"""
        res = self.client().post('/new_task', json=self.task)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/tasks')
        self.assertEqual(res.status_code, 200)
        self.assertIn('ls', str(res.data))

    def test_get_task_output(self):
        """Test API can get the output of a single task using it's id."""
        rv = self.client().post('/new_task', json=self.task)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/get_output/{}'.format(result_in_json['id'])
        )
        self.assertEqual(result.status_code, 200)
        self.assertIn('ls', str(result.data))

    def test_get_missing_task_output(self):
        """Test API returns 404 for missing task"""
        res = self.client().get('/get_output/{}'
                                .format('609128054724352685602766'))
        self.assertEqual(res.status_code, 404)
