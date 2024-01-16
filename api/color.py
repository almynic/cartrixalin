from flask import Blueprint, request, jsonify

from constants.http import HTTP_STATUS_CREATED, HTTP_STATUS_OK
from services.color import ColorService


def to_dict_list(colors):
    return [color.to_dict() for color in colors]


color_api = Blueprint('color_api', __name__, url_prefix='/api/colors')


@color_api.route('/', methods=['GET'])
def get_colors():
    colors = ColorService.get_all()
    return jsonify(to_dict_list(colors)), HTTP_STATUS_OK


@color_api.route('', methods=['POST'])
def create_color():
    new_color = ColorService.create(request.json)
    return jsonify(new_color.to_dict()), HTTP_STATUS_CREATED


@color_api.route('/<int:id>', methods=['PUT'])
def update_color(id):
    updated_color = ColorService.update(id, request.json)
    return jsonify(updated_color.to_dict()), HTTP_STATUS_OK


@color_api.route('/<int:id>', methods=['GET'])
def get_color(id):
    color = ColorService.get_by_id(id)
    return jsonify(color.to_dict())


@color_api.route('/<int:id>', methods=['DELETE'])
def delete_color(id):
    ColorService.delete(id)
    return jsonify({'message': 'Color deleted'}), HTTP_STATUS_OK
