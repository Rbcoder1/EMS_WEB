from flask import Flask
from app.Admin.views import admin
from app.User.views import user
from app.Main.main import main


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(user)

    return app