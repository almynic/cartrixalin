import unittest
from unittest.mock import patch

from flask import Flask
from flask_testing import TestCase

from api.brand import brand_api


class BrandApiTestCase(TestCase):
    """

    BrandApiTestCase

    TestCase class for testing the Brand API endpoints.

    Methods:
    - create_app: Creates a Flask application instance for testing.
    - test_get_brand_by_id: Tests the GET request for retrieving a brand by its ID.
    - test_get_all_brands: Tests the GET request for retrieving all brands.
    - test_create_brand: Tests the POST request for creating a new brand.
    - test_update_brand: Tests the PUT request for updating a brand.
    - test_delete_brand: Tests the DELETE request for deleting a brand.

    """

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(brand_api)
        return app

    @patch('services.brand.BrandService.get_by_id')
    def test_get_brand_by_id(self, mock_get_by_id):
        # Setup mock return value
        mock_get_by_id.return_value = MockBrand(id=1, name='Test Brand')

        # Perform GET request
        response = self.client.get('/api/brands/1')

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'id': 1, 'name': 'Test Brand'})
        mock_get_by_id.assert_called_once_with(1)

    @patch('services.brand.BrandService.get_all')
    def test_get_all_brands(self, mock_get_all):
        mock_get_all.return_value = [MockBrand(id=1, name='Brand A'), MockBrand(id=2, name='Brand B')]

        response = self.client.get('/api/brands/')

        expected_result = [{'id': 1, 'name': 'Brand A'}, {'id': 2, 'name': 'Brand B'}]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
        mock_get_all.assert_called_once()

    @patch('services.brand.BrandService.create')
    def test_create_brand(self, mock_create):
        mock_create.return_value = MockBrand(id=1, name='New Brand')
        brand_data = {'name': 'New Brand'}

        response = self.client.post('/api/brands/', json=brand_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'id': 1, 'name': 'New Brand'})
        mock_create.assert_called_once_with(brand_data)

    @patch('services.brand.BrandService.update')
    def test_update_brand(self, mock_update_brand):
        mock_update_brand.return_value = MockBrand(id=1, name='Updated Brand')
        updated_data = {'name': 'Updated Brand'}

        response = self.client.put('/api/brands/1', json=updated_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'id': 1, 'name': 'Updated Brand'})
        mock_update_brand.assert_called_once_with(1, updated_data)

    @patch('services.brand.BrandService.delete')
    def test_delete_brand(self, mock_delete):
        response = self.client.delete('/api/brands/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Brand deleted'})
        mock_delete.assert_called_once_with(1)


# Define MockBrand class for testing
class MockBrand:
    """
    Initializes a new instance of the MockBrand class.

    :param id: The unique identifier of the brand.
    :type id: int
    :param name: The name of the brand.
    :type name: str
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


if __name__ == '__main__':
    unittest.main()
