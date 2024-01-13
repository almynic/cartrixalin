from flask import Blueprint, abort, request, render_template
from flask import jsonify

from database import db

from constants.http import HTTP_STATUS_NOT_FOUND, HTTP_STATUS_CREATED, HTTP_STATUS_OK
from models.toner import BRAND, Toner, NAME, COLOR, SCOPE_OF_DELIVERY, CARTRIDGE_NO, COMPATIBLE_PRINTERS, \
    MAX_PRINTABLE_PAGES

toner_api = Blueprint('toner_api', __name__, url_prefix='/api/toners')
toner_views = Blueprint('toner_views', __name__, url_prefix='/toners')


@toner_api.route('', methods=['GET'])
def get_toners():
    """
    Retrieve all toners.

    :return: A JSON object containing a list of all toners.
    :rtype: flask.Response
    """
    toners = Toner.query.all()
    toner_list = [t.to_dict() for t in toners]
    return jsonify(toner_list)


@toner_api.route('', methods=['POST'])
def create_toner():
    new_toner = Toner()
    populate_toner_details(new_toner)
    db.session.add(new_toner)
    db.session.commit()
    return jsonify(new_toner.to_dict()), HTTP_STATUS_CREATED


@toner_api.route('/<int:id>', methods=['PUT'])
def update_toner(id):
    toner = get_toner_by_id(id)
    populate_toner_details(toner)
    db.session.commit()
    return jsonify(toner.to_dict()), HTTP_STATUS_OK


@toner_api.route('/<int:id>', methods=['GET'])
def get_toner(id):
    """
    Retrieve the details of a toner by its ID.

    :param id: The ID of the toner.
    :return: A JSON representation of the toner object.
    :rtype: str
    """
    toner = get_toner_by_id(id)
    return jsonify(toner.to_dict())


@toner_views.route('', methods=['GET'])
def show_all_toners():
    toners = Toner.query.all()
    return render_template('all-toners.html', toners=toners)


@toner_views.route('/<int:id>', methods=['GET'])
def show_toner(id):
    toner = get_toner_by_id(id)
    return render_template('toner.html', toner=toner)


@toner_api.route('/<int:id>', methods=['DELETE'])
def delete_toner(id):
    """
    Delete Toner

    Deletes a toner from the database.

    :param id: The ID of the toner to be deleted.
    :return: A JSON response indicating the success of the deletion.
    """
    toner = get_toner_by_id(id)
    db.session.delete(toner)
    db.session.commit()
    return jsonify({'message': 'Toner deleted'}), HTTP_STATUS_OK


def get_toner_by_id(id):
    """
    Get a Toner instance if it exists based on the given ID.
    :param id: The ID of the toner to check.
    :type id: int
    :return: The toner if it exists.
    :rtype: Toner
    :raises HTTPException: If the toner is not found.
    """
    toner = Toner.query.get(id)
    if toner is None:
        abort(HTTP_STATUS_NOT_FOUND, description="Toner not found")
    return toner


def populate_toner_details(toner):
    """
    Populate the details of a toner from request data.
    """
    toner.brand = request.json[BRAND]
    toner.name = request.json[NAME]
    toner.color = request.json[COLOR]
    toner.scope_of_delivery = request.json[SCOPE_OF_DELIVERY]
    toner.cartridge_no = request.json[CARTRIDGE_NO]
    toner.compatible_printers = request.json[COMPATIBLE_PRINTERS]
    toner.max_printable_pages = request.json[MAX_PRINTABLE_PAGES]
