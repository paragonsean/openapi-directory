from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_response import AuthResponse
from openapi_server.models.model_error import ModelError
from openapi_server import util


async def auth_default_login_post(request: web.Request, username, password) -> web.Response:
    """auth_default_login_post

    Returns Native Ads Publisher API token

    :param username: Native Ads Publisher username
    :type username: str
    :param password: Native Ads Publisher password
    :type password: str

    """
    return web.Response(status=200)
