from flask import Flask

from app.routes.food_routes import food_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(food_bp)

    return app
