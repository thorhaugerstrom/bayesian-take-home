from flask import Flask
from .models import init_db, get_db_connection

def create_app():
    app = Flask(__name__)

    from .routes import bp as api_bp
    app.register_blueprint(api_bp)

    return app