from flask import abort

from constants.http import HTTP_STATUS_NOT_FOUND
from database import db
from models.brand import Brand


class BrandService:
    """
    BrandService

    Class implementing CRUD operations for managing brands in a database.

    Methods:
    - create(data): Creates a new brand with the given data and saves it to the database.
        Parameters:
            - data (dict): A dictionary containing the data for the new brand.
        Returns:
            - new_brand (Brand): The newly created brand.

    - get_all(): Retrieves all brands from the database.
        Returns:
            - brands (list): A list of all brands.

    - get_by_id(id): Retrieves a brand from the database with the specified ID.
        Parameters:
            - id (int): The ID of the brand to retrieve.
        Returns:
            - brand (Brand): The brand with the specified ID.
        Raises:
            - HTTPException: If the brand with the specified ID is not found.

    - update(id, data): Updates the data of a brand in the database with the specified ID.
        Parameters:
            - id (int): The ID of the brand to update.
            - data (dict): A dictionary containing the updated data for the brand.
        Returns:
            - brand (Brand): The updated brand.
        Raises:
            - HTTPException: If the brand with the specified ID is not found.

    - delete(id): Deletes a brand from the database with the specified ID.
        Parameters:
            - id (int): The ID of the brand to delete.
    """
    @staticmethod
    def create(data):
        new_brand = Brand(**data)
        db.session.add(new_brand)
        db.session.commit()
        return new_brand

    @staticmethod
    def get_all():
        return Brand.query.all()

    @staticmethod
    def get_by_id(id):
        toner = Brand.query.get(id)
        if toner is None:
            abort(HTTP_STATUS_NOT_FOUND, description="Toner not found")
        return toner

    @staticmethod
    def update(id, data):
        brand = BrandService.get_by_id(id)
        for key, value in data.items():
            setattr(brand, key, value)
        db.session.commit()
        return brand

    @staticmethod
    def delete(id):
        brand = BrandService.get_by_id(id)
        db.session.delete(brand)
        db.session.commit()
