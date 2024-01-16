from flask import abort

from constants.http import HTTP_STATUS_NOT_FOUND
from database import db
from models.toner import Toner


class TonerService:
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
        new_toner = Toner(**data)
        db.session.add(new_toner)
        db.session.commit()
        return new_toner

    @staticmethod
    def get_all():
        return Toner.query.all()

    @staticmethod
    def get_by_id(id):
        toner = Toner.query.get(id)
        if toner is None:
            abort(HTTP_STATUS_NOT_FOUND, description="Toner not found")
        return toner

    @staticmethod
    def update(id, data):
        toner = TonerService.get_by_id(id)
        for key, value in data.items():
            setattr(toner, key, value)
        db.session.commit()
        return toner

    @staticmethod
    def delete(id):
        toner = TonerService.get_by_id(id)
        db.session.delete(toner)
        db.session.commit()
