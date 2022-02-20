from flask import Flask

from app.board import Board


board = Board()


class Config:
    SECRET_KEY = "I_am_very_secret"


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    from app.views import blueprint

    app.register_blueprint(blueprint)

    return app
