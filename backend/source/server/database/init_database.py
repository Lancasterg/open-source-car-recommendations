from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def init_database(app: Flask):
    db = SQLAlchemy()

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return db


def get_db(app: Flask) -> SQLAlchemy:
    db = SQLAlchemy()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    return db


if __name__ == "__main__":
    application = Flask(__name__)
    init_database(application)
