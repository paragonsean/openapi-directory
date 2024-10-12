from typing import List, Dict
from aiohttp import web

from openapi_server.models.oauth_v1_device_code import OauthV1DeviceCode
from openapi_server import util


async def create_device_code(request: web.Request, client_sid, scopes, audiences=None) -> web.Response:
    """create_device_code

    Issues a new Access token (optionally identity_token &amp; refresh_token) in exchange of Oauth grant

    :param client_sid: A 34 character string that uniquely identifies this OAuth App.
    :type client_sid: str
    :param scopes: An Array of scopes for authorization request
    :type scopes: List[str]
    :param audiences: An array of intended audiences for token requests
    :type audiences: List[str]

    """
    return web.Response(status=200)
