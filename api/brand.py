from flask import Blueprint, request, jsonify

from constants.http import HTTP_STATUS_CREATED, HTTP_STATUS_OK
from services.brand import BrandService


def to_dict_list(brands):
    return [brand.to_dict() for brand in brands]


brand_api = Blueprint('brand_api', __name__, url_prefix='/api/brands')


@brand_api.route('/', methods=['GET'])
def get_brands():
    brands = BrandService.get_all()
    return jsonify(to_dict_list(brands)), HTTP_STATUS_OK


@brand_api.route('/', methods=['POST'])
def create_brand():
    new_brand = BrandService.create(request.json)
    return jsonify(new_brand.to_dict()), HTTP_STATUS_CREATED


@brand_api.route('/<int:id>', methods=['PUT'])
def update_brand(id):
    updated_brand = BrandService.update(id, request.json)
    return jsonify(updated_brand.to_dict()), HTTP_STATUS_OK


@brand_api.route('/<int:id>', methods=['GET'])
def get_brand(id):
    brand = BrandService.get_by_id(id)
    return jsonify(brand.to_dict())


@brand_api.route('/<int:id>', methods=['DELETE'])
def delete_brand(id):
    BrandService.delete(id)
    return jsonify({'message': 'Brand deleted'}), HTTP_STATUS_OK
