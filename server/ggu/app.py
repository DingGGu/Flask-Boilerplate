import importlib
import os

from flask import Flask, jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.middleware.proxy_fix import ProxyFix
from sentry_sdk.integrations.flask import FlaskIntegration

from ..clients.sentry import init_sentry
from ..app_config import AppConfig


def create_app(config: AppConfig) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    init_sentry([FlaskIntegration()])

    from . import apis
    for api in apis.__all__:
        bp = importlib.import_module(f'..apis.{api}', __name__)
        bp.init(app)

    @app.route('/ping')
    def ping():
        return 'pong!'

    def spec_json():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "ggu"
        return jsonify(swag)

    if os.environ.get('PROJECT_ENV') == 'development':
        app.add_url_rule('/swagger.json', view_func=spec_json)
        app.register_blueprint(get_swaggerui_blueprint(
            base_url='/swagger',
            api_url='/swagger.json'
        ), url_prefix='/swagger')

    return app
