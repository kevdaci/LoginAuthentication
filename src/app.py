from flask import Flask, jsonify
from flask_session import Session
from database.database import db
from controller.auth import auth
from controller.profile import profile
import os

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        SESSION_PERMANENT = False,
        SESSION_TYPE = "filesystem"
    )
    # app.config.from_pyfile('config.py')
    db.app = app
    db.init_app(app)
    db.create_all()
    Session(app)
    app.register_blueprint(auth)
    app.register_blueprint(profile)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)