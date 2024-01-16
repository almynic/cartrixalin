from flask import Blueprint, render_template

index_views = Blueprint('index_views', __name__, url_prefix='/')


@index_views.route('/', methods=['GET'])
def show_all_brands():
    return render_template('index.html')

