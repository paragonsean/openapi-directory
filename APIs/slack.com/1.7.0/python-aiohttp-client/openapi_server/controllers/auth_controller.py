from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_revoke_error_schema import AuthRevokeErrorSchema
from openapi_server.models.auth_revoke_schema import AuthRevokeSchema
from openapi_server.models.auth_test_error_schema import AuthTestErrorSchema
from openapi_server.models.auth_test_success_schema import AuthTestSuccessSchema
from openapi_server import util


async def auth_revoke(request: web.Request, token, test=None) -> web.Response:
    """auth_revoke

    Revokes a token.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param test: Setting this parameter to &#x60;1&#x60; triggers a _testing mode_ where the specified token will not actually be revoked.
    :type test: bool

    """
    return web.Response(status=200)


async def auth_test(request: web.Request, token) -> web.Response:
    """auth_test

    Checks authentication &amp; identity.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str

    """
    return web.Response(status=200)
