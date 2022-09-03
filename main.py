import os

from app import create_app

PROFILE = 'PROFILE'
app = create_app(os.getenv(PROFILE, 'prod'))

if __name__ == '__main__':
    app.run(host=app.config['APP_HOST'], port=app.config['APP_PORT'])
