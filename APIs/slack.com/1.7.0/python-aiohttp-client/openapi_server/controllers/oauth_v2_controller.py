from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def oauth_v2_access(request: web.Request, code, client_id=None, client_secret=None, redirect_uri=None) -> web.Response:
    """oauth_v2_access

    Exchanges a temporary OAuth verifier code for an access token.

    :param code: The &#x60;code&#x60; param returned via the OAuth callback.
    :type code: str
    :param client_id: Issued when you created your application.
    :type client_id: str
    :param client_secret: Issued when you created your application.
    :type client_secret: str
    :param redirect_uri: This must match the originally submitted URI (if one was sent).
    :type redirect_uri: str

    """
    return web.Response(status=200)
