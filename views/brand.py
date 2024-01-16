from flask import Blueprint, render_template, flash, redirect, url_for

from forms.brand import BrandForm
from services.brand import BrandService

brand_views = Blueprint('brand_views', __name__, url_prefix='/brands')


@brand_views.route('/', methods=['GET'])
def show_all_brands():
    brands = BrandService.get_all()
    return render_template('brand/list.html', brands=brands)


@brand_views.route('/<int:brand_id>', methods=['GET'])
def show_brand(brand_id):
    brand = BrandService.get_by_id(brand_id)
    return render_template('brand/details.html', brand=brand)


@brand_views.route('/new', methods=['GET', 'POST'])
def new_brand():
    form = BrandForm()
    if form.validate_on_submit():
        BrandService.create(form.to_dict())
        flash('Brand {} has been added!'.format(form.name.data))
        return redirect(url_for('brand_views.show_all_brands'))
    return render_template('brand/new.html', form=form)


@brand_views.route('/<int:brand_id>/delete', methods=['POST'])
def delete_brand(brand_id):
    # access the id from posted data instead of a form

    if brand_id is not None:
        deleted_brand = BrandService.delete(brand_id)
        if deleted_brand:
            flash(f'Brand {deleted_brand.name} has been deleted!')
            return redirect(url_for('brand_views.show_all_brands'))

    flash('An error has occurred. Deletion unsuccessful.')
    return redirect(url_for('brand_views.show_all_brands'))
