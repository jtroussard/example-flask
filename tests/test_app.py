import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def tearDown(self):
        # Clean up after the test
        pass

    def test_hello_name(self):
        # Test the /hello/<name> endpoint
        response = self.app.get('/hello/John')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello John!')

if __name__ == '__main__':
    unittest.main()
