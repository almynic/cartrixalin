from flask import Flask

from database import db
from routes.toner_api import toner_api, toner_views


def define_routes(application):
    # Register api routes
    application.register_blueprint(toner_api)

    # Register views routes
    application.register_blueprint(toner_views)


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///cartixalin.db')

    if config:
        app.config.from_object(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    define_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
