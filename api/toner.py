from flask import Blueprint, request, render_template, jsonify

from constants.http import HTTP_STATUS_CREATED, HTTP_STATUS_OK
from services.toner import TonerService


def to_dict_list(toners):
    return [toner.to_dict() for toner in toners]


toner_api = Blueprint('toner_api', __name__, url_prefix='/api/toners')


@toner_api.route('/', methods=['GET'])
def get_toners():
    toners = TonerService.get_all()
    return jsonify(to_dict_list(toners)), HTTP_STATUS_OK


@toner_api.route('', methods=['POST'])
def create_toner():
    new_toner = TonerService.create(request.json)
    return jsonify(new_toner.to_dict()), HTTP_STATUS_CREATED


@toner_api.route('/<int:id>', methods=['PUT'])
def update_toner(id):
    updated_toner = TonerService.update_toner(id, request.json)
    return jsonify(updated_toner.to_dict()), HTTP_STATUS_OK


@toner_api.route('/<int:id>', methods=['GET'])
def get_toner(id):
    toner = TonerService.get_by_id(id)
    return jsonify(toner.to_dict())


@toner_api.route('/<int:id>', methods=['DELETE'])
def delete_toner(id):
    TonerService.delete(id)
    return jsonify({'message': 'Toner deleted'}), HTTP_STATUS_OK
