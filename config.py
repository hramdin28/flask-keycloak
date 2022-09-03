import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(32))
    DEBUG = False
    TESTING = False
    APP_PORT = 5000
    APP_HOST = '127.0.0.1'


class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_CHECK_DEFAULT = False
    ENV = 'development'
    OIDC_CLIENT_SECRETS = 'resources/env/dev/client_secrets.json'
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    OIDC_REQUIRE_VERIFIED_EMAIL = False
    OIDC_USER_INFO_ENABLED = True
    OIDC_OPENID_REALM = 'flaskRealm'
    OIDC_SCOPES = ['openid', 'email', 'profile']
    OIDC_INTROSPECTION_AUTH_METHOD = 'client_secret_post'
    OIDC_RESOURCE_SERVER_ONLY = False


class ProductionConfig(Config):
    DEBUG = False
    APP_PORT = 8081
    APP_HOST = '0.0.0.0'
    OIDC_CLIENT_SECRETS = 'resources/env/prod/client_secrets.json'
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    OIDC_REQUIRE_VERIFIED_EMAIL = False
    OIDC_USER_INFO_ENABLED = True
    OIDC_OPENID_REALM = 'flaskRealm'
    OIDC_SCOPES = ['openid', 'email', 'profile']
    OIDC_INTROSPECTION_AUTH_METHOD = 'client_secret_post'


config_by_profile = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
