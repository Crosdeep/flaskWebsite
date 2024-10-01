from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    db = SQLAlchemy()
    DB_NAME = "database.db"
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'WOEFKPWO'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    return app