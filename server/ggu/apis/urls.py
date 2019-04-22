import flask
from sentry_sdk import last_event_id

from .resp import Responser

bp = flask.Blueprint('api', __name__, url_prefix='/api')


@bp.app_errorhandler(500)
def internal_server_error(e=None):
    event_id = last_event_id()

    if flask.request.path.startswith('/api/'):
        return Responser().error(500, f'내부 서버 오류 report_id={event_id}')
    return e


@bp.app_errorhandler(404)
def page_not_found(e=None):
    if flask.request.path.startswith('/api/'):
        return Responser().error(404, '페이지를 찾을 수 없습니다.')
    return e


def init(app: flask.Flask):
    app.register_blueprint(bp)
    return app
