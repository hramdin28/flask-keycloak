from flask import Blueprint
from flask_restx import Api

from app.main.controller.app_controller import api as app_api

API = '/api'
api_bp = Blueprint(
    'api_bp', __name__
)
api = Api(api_bp, title="Api", version="1.0", description="RESTX API")
api.add_namespace(app_api, path=API)
