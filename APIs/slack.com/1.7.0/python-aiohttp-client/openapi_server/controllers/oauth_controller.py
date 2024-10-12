from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def oauth_access(request: web.Request, client_id=None, client_secret=None, code=None, redirect_uri=None, single_channel=None) -> web.Response:
    """oauth_access

    Exchanges a temporary OAuth verifier code for an access token.

    :param client_id: Issued when you created your application.
    :type client_id: str
    :param client_secret: Issued when you created your application.
    :type client_secret: str
    :param code: The &#x60;code&#x60; param returned via the OAuth callback.
    :type code: str
    :param redirect_uri: This must match the originally submitted URI (if one was sent).
    :type redirect_uri: str
    :param single_channel: Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://api.slack.com/legacy-workspace-apps).
    :type single_channel: bool

    """
    return web.Response(status=200)


async def oauth_token(request: web.Request, client_id=None, client_secret=None, code=None, redirect_uri=None, single_channel=None) -> web.Response:
    """oauth_token

    Exchanges a temporary OAuth verifier code for a workspace token.

    :param client_id: Issued when you created your application.
    :type client_id: str
    :param client_secret: Issued when you created your application.
    :type client_secret: str
    :param code: The &#x60;code&#x60; param returned via the OAuth callback.
    :type code: str
    :param redirect_uri: This must match the originally submitted URI (if one was sent).
    :type redirect_uri: str
    :param single_channel: Request the user to add your app only to a single channel.
    :type single_channel: bool

    """
    return web.Response(status=200)


async def oauth_v2_access_0(request: web.Request, code, client_id=None, client_secret=None, redirect_uri=None) -> web.Response:
    """oauth_v2_access_0

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
