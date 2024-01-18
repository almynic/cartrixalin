from flask import render_template, Blueprint, flash, redirect, url_for, request

from forms.toner import TonerForm
from services.toner import TonerService

toner_views = Blueprint('toner_views', __name__, url_prefix='/toners')


@toner_views.route('/', methods=['GET'])
def show_all_toners():
    toners = TonerService.get_all()
    return render_template('toner/list.html', toners=toners)


@toner_views.route('/<int:id>', methods=['GET'])
def show_toner(id):
    toner = TonerService.get_by_id(id)
    return render_template('toner/details.html', toner=toner)


@toner_views.route('/new', methods=['GET', 'POST'])
def new_toner():
    form = TonerForm()
    if form.validate_on_submit():
        TonerService.create(form.to_dict())
        flash('Toner {} has been added!'.format(form.name.data))
        return redirect(url_for('toner_views.show_all_toners'))
    return render_template('toner/new.html', form=form)


@toner_views.route('/delete', methods=['POST'])
def delete_toner():
    # access the id from posted data instead of a form
    toner_id = request.form.get('id')

    if toner_id is not None:
        deleted_toner = TonerService.delete(toner_id)
        if deleted_toner:
            flash(f'Toner {deleted_toner.name} has been deleted!')
            return redirect(url_for('toner_views.show_all_toners'))

    flash('An error has occurred. Deletion unsuccessful.')
    return redirect(url_for('toner_views.show_all_toners'))
