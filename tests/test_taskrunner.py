import os
import unittest
from app import application


class BasicTestCase(unittest.TestCase):
    """This class represents the basic test case"""

    def setUp(self) -> None:
        application.config['TESTING'] = True
        self.application = application.test_client()

    def tearDown(self) -> None:
        pass

    def test_app_is_up(self):
        res = self.application.get('/', follow_redirects=True)
        self.assertEqual(res.status_code, 200)

    if __name__ == "__main__":
        unittest.main()