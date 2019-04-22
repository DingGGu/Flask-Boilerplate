import typing
from datetime import datetime

import flask
from flask import Response

from ...tz import UTC


class Responser:
    time = datetime.now(tz=UTC)

    def error(self, code: int = 400, message: typing.Optional[str] = None, **kwargs):
        resp: Response = flask.jsonify(
            success=False,
            time=self.time,
            message=message,
            code=code,
            **kwargs
        )

        resp.headers.add("Access-Control-Allow-Origin", "*")
        resp.headers.add("Access-Control-Allow-Headers", "*")
        resp.headers.add("Access-Control-Allow-Methods", "*")
        return resp, code

    def success(self, data: typing.Optional[dict] = None, **kwargs):
        respond = dict(
            time=self.time,
        )

        if data is not None:
            respond.update(dict(data=data))

        if kwargs:
            respond.update(kwargs)

        resp: Response = flask.jsonify(
            success=True,
            **respond
        )

        resp.headers.add("Access-Control-Allow-Origin", "*")
        resp.headers.add("Access-Control-Allow-Headers", "*")
        resp.headers.add("Access-Control-Allow-Methods", "*")

        return resp
