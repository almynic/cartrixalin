from flask import abort

from constants.http import HTTP_STATUS_NOT_FOUND
from database import db
from models.ink import Ink


class InkService(object):
    """
    A class that provides CRUD operations for Toners in a database.

    Functions:
        create(data):
            Creates a new Toner record in the database.

            Parameters:
                data (dict): A dictionary representing the attributes of the new Toner.

            Returns:
                Toner: The newly created Toner record.

        get_all():
            Retrieves all the Toner records from the database.

            Returns:
                List[Toner]: A list containing all the Toner records.

        get_by_id(id):
            Retrieves a specific Toner record from the database based on its ID.

            Parameters:
                id (int): The ID of the Toner to retrieve.

            Returns:
                Toner: The Toner record with the specified ID.

            Raises:
                HTTPError: If no Toner record is found with the given ID.

        update(id, data):
            Updates the attributes of a specific Toner record in the database.

            Parameters:
                id (int): The ID of the Toner to update.
                data (dict): A dictionary representing the updated attributes of the Toner.

            Returns:
                Toner: The updated Toner record.

        delete(id):
            Deletes a specific Toner record from the database.

            Parameters:
                id (int): The ID of the Toner to delete.

            Returns:
                None
    """

    @staticmethod
    def create(data):
        new_ink = Ink(**data)
        db.session.add(new_ink)
        db.session.commit()
        return new_ink

    @staticmethod
    def get_all():
        return Ink.query.all()

    @staticmethod
    def get_by_id(id):
        ink = Ink.query.get(id)
        if ink is None:
            abort(HTTP_STATUS_NOT_FOUND, description="Ink not found")
        return ink

    @staticmethod
    def update(id, data):
        ink = InkService.get_by_id(id)
        for key, value in data.items():
            setattr(ink, key, value)
        db.session.commit()
        return ink

    @staticmethod
    def delete(id):
        ink = InkService.get_by_id(id)
        db.session.delete(ink)
        db.session.commit()
