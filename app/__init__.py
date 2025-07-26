from flask import Flask
from app.routes.main_routes import main_routes
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default-secret")

    # Register routes
    app.register_blueprint(main_routes)

    return app