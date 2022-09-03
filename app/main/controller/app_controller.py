import json

import requests
from flask import current_app, g
from flask_oidc import OpenIDConnect
from flask_restx import Resource

from app.main.api.app_api import AppApi
from app.main.dto.auth_dto import AuthDto

api = AppApi.api
auth_model = AppApi.auth_model
oidc = OpenIDConnect(current_app)


@api.route("/")
class AppController(Resource):
    def get(self):
        if oidc.user_loggedin:
            return 'Welcome %s' % oidc.user_getfield('name')
        else:
            return 'Not logged in'


@api.route("/greetings")
class AppControllerToken(Resource):
    def get(self):
        info = oidc.user_getinfo(['preferred_username', 'email', 'sub', 'name'])
        return json.dumps('Welcome %s' % info.get('name'))


@api.route("/login")
class AppControllerLogin(Resource):
    @oidc.require_login
    def get(self):
        info = oidc.user_getinfo(['preferred_username', 'email', 'sub', 'name'])

        username = info.get('preferred_username')
        email = info.get('email')
        user_id = info.get('sub')
        name = info.get('name')
        print(username)
        print(name)
        print(email)
        print(user_id)

        return 'Login details: id:%s, username:%s, name:%s,  email:%s' % (
            user_id, username, name, email)


@api.route("/logout")
class AppControllerLogOut(Resource):
    def get(self):
        if oidc.user_loggedin:
            user = oidc.user_getfield('name')
            oidc.logout()
            return 'Bye %s' % user
        return 'Logged out'


@api.expect(auth_model, validate=True)
@api.route("/request_token")
class AppControllerRequestToken(Resource):
    def post(self):
        keycloak = oidc.client_secrets
        payload = api.payload
        auth_dto = AuthDto(
            client_id=keycloak['client_id'],
            client_secret=keycloak['client_secret'],
            username=payload['username'],
            password=payload['password'],
        )
        idp_resonse = requests.post(keycloak['token_uri'], data=auth_dto.dict()).json()

        return idp_resonse


@api.route('/token')
class BearerToken(Resource):
    @oidc.require_login
    def get(self):
        access_token = oidc.get_access_token()
        return 'Authorization: Bearer %s' % access_token


@api.route('/token_required_resource')
class TokenResource(Resource):
    @oidc.accept_token(require_token=True)
    def get(self):
        return json.dumps({'hello': ' %s' % g.oidc_token_info['sub']})
