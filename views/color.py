from flask import Blueprint, render_template, flash, redirect, url_for

from forms.color import ColorForm
from services.color import ColorService

color_views = Blueprint('color_views', __name__, url_prefix='/colors')


@color_views.route('/', methods=['GET'])
def show_all_colors():
    colors = ColorService.get_all()
    return render_template('color/list.html', colors=colors)


@color_views.route('/<int:color_id>', methods=['GET'])
def show_color(color_id):
    color = ColorService.get_by_id(color_id)
    return render_template('color/details.html', color=color)


@color_views.route('/new', methods=['GET', 'POST'])
def new_color():
    form = ColorForm()
    if form.validate_on_submit():
        ColorService.create(form.to_dict())
        flash('Toner {} has been added!'.format(form.name.data))
        return redirect(url_for('color_views.show_all_colors'))
    return render_template('color/new.html', form=form)
