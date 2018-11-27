from flask import Flask
from app.models.base import db

def create_app():
    app = Flask(__name__)
    print("id为" + str(id(app)) + "的app注册")

    app.config.from_object('app.secure')
    app.config.from_object('app.settings')

    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)

    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
