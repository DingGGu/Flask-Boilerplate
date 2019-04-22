import os
import typing

import sentry_sdk
from sentry_sdk.integrations import Integration


def init_sentry(integrations: typing.List[Integration] = None):
    sentry_sdk.init(
        integrations=integrations,
        send_default_pii=True,
        environment=os.environ.get('PROJECT_ENV', 'development')
    )
