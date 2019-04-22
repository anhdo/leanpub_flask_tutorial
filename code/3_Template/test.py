import unittest
from app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'Hello'

    def test_specific_hello(self):
        response = self.app.get('/hello/dummy')
        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'Hello dummy'
    
    def test_double(self):
        response = self.app.get('/double/2')
        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'Double of 2 is 4'
    
    def test_double_wrong_type(self):
        response = self.app.get('/double/two')
        assert response.status_code == 404
    
    def test_old_hello(self):
        response = self.app.get('/old_hello')
        assert response.status_code == 302
        assert response.location.endswith('/hello')

    def test_custom_code(self):
        response = self.app.get('/custom_code')
        assert response.status_code == 201
        assert response.get_data(as_text=True) == 'custom code'
