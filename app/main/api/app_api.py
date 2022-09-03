from flask_restx import Namespace, fields


class AppApi:
    api = Namespace('API', description='API related operations')

    auth_model = api.model('parameter', {
        'username': fields.String(required=True),
        'password': fields.String(required=True),
    }, strict=True)
