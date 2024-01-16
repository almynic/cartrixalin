from flask import abort

from constants.http import HTTP_STATUS_NOT_FOUND
from database import db
from models.color import Color


class ColorService:
    """ColorService class provides methods for CRUD operations on colors.

    Attributes:
        None

    Methods:
        create(data):
            Creates a new color instance with the provided data and adds it to the database.

        get_all():
            Retrieves all color instances from the database.
            Returns:
                List of color instances.

        get_by_id(id):
            Retrieves a color instance from the database based on the provided id.
            Args:
                id (int): The id of the color instance to retrieve.
            Returns:
                The color instance with the provided id.
            Raises:
                HTTPException: If the color instance is not found in the database.

        update(id, data):
            Updates the attributes of a color instance with the provided data.
            Args:
                id (int): The id of the color instance to update.
                data (dict): The data used for updating the color instance attributes.
            Returns:
                The updated color instance.

        delete(id):
            Deletes a color instance from the database based on the provided id.
            Args:
                id (int): The id of the color instance to delete.
    """
    @staticmethod
    def create(data):
        new_color = Color(**data)
        db.session.add(new_color)
        db.session.commit()
        return new_color

    @staticmethod
    def get_all():
        return Color.query.all()

    @staticmethod
    def get_by_id(id):
        color = Color.query.get(id)
        if color is None:
            abort(HTTP_STATUS_NOT_FOUND, description="Toner not found")
        return color

    @staticmethod
    def update(id, data):
        color = ColorService.get_by_id(id)
        for key, value in data.items():
            setattr(color, key, value)
        db.session.commit()
        return color

    @staticmethod
    def delete(id):
        color = ColorService.get_by_id(id)
        db.session.delete(color)
        db.session.commit()
