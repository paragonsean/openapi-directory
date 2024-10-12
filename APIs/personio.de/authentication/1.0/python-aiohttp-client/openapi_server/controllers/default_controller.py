from typing import List, Dict
from aiohttp import web

from openapi_server.models.authentication_token_response import AuthenticationTokenResponse
from openapi_server import util


async def auth_post(request: web.Request, client_id, client_secret) -> web.Response:
    """auth_post

    Request Authentication Token

    :param client_id: Client id of the downloaded credentials file
    :type client_id: str
    :param client_secret: Client secret of the downloaded credentials file
    :type client_secret: str

    """
    return web.Response(status=200)
