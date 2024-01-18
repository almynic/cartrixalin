import os

from flask import Flask
from flask_migrate import Migrate

from api.brand import brand_api
from api.color import color_api
from api.toner import toner_api
from database import db
from views.brand import brand_views
from views.color import color_views
from views.index import index_views
from views.toner import toner_views

SECRET_KEY = os.urandom(32)


def define_routes(application):

    # Register views routes
    application.register_blueprint(toner_views)
    application.register_blueprint(color_views)
    application.register_blueprint(brand_views)

    # Register root view
    application.register_blueprint(index_views)

    # Register api routes
    application.register_blueprint(toner_api)
    application.register_blueprint(color_api)
    application.register_blueprint(brand_api)


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///cartixalin.db')
    app.config['SECRET_KEY'] = SECRET_KEY

    if config:
        app.config.from_object(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db)  # initialize flask-migrate

    define_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
