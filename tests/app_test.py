import unittest
from flask_testing import TestCase
from cartrixalin import create_app
from constants.http import HTTP_STATUS_CREATED, HTTP_STATUS_NOT_FOUND
from database import db


class CustomAssertions:
    @staticmethod
    def assert_equal_in_json(json_data, keys_values):
        for key, value in keys_values.items():
            assert key in json_data, f"Key '{key}' not found in JSON data"
            assert json_data[key] == value, f"Expected '{value}', got '{json_data[key]}' for key '{key}'"


class AppTest(TestCase, CustomAssertions):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        config = {'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'}
        app = create_app(config)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_toner(self):
        toner_data = {
            'brand': 'Test Brand',
            'name': 'Test Name',
            'color': 'Test Color',
            'scope_of_delivery': 'Test Scope',
            'cartridge_no': 'Test No',
            'compatible_printers': 'Test Printers',
            'max_printable_pages': 1000
        }
        response = self.client.post('/api/toners', json=toner_data)
        self.assertEqual(HTTP_STATUS_CREATED, response.status_code)
        self.assert_equal_in_json(response.get_json(), toner_data)

    def test_get_toner_by_id(self):
        response = self.client.get('/api/toners/1')
        self.assertEqual(HTTP_STATUS_NOT_FOUND, response.status_code)


if __name__ == '__main__':
    unittest.main()
