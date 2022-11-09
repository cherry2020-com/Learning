import os
from flask import Flask
from cfenv import AppEnv
from flask import request
from flask import abort

from sap import xssec

app = Flask(__name__)
env = AppEnv()

port = int(os.environ.get('PORT', 3000))
uaa_service = env.get_service(name='pyuaa').credentials


@app.route('/')
def hello():
    if 'authorization' not in request.headers:
        abort(403)
    access_token = request.headers.get('authorization')[7:]
    security_context = xssec.create_security_context(access_token, uaa_service)
    isAuthorized = security_context.check_scope('openid')
    if not isAuthorized:
        abort(403)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
