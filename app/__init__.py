from flask import Flask
from flask_principal import Principal

from config import config_by_profile


def create_app(profile: str):
    print(f"Profile: {profile}")
    app = Flask(__name__)
    app.config.from_object(config_by_profile[profile])
    with app.app_context():
        app._principal = Principal(app, use_sessions=False)
        from app.main import api_bp
        app.register_blueprint(api_bp)
    return app
