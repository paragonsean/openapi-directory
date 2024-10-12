from typing import List, Dict
from aiohttp import web

from openapi_server.models.invalid_token import InvalidToken
from openapi_server.models.login_response import LoginResponse
from openapi_server.models.sample1 import Sample1
from openapi_server import util


async def login_post(request: web.Request, body) -> web.Response:
    """Log in to get an API token

    Submit your email and password to get an API token

    :param body: The login payload
    :type body: dict | bytes

    """
    body = Sample1.from_dict(body)
    return web.Response(status=200)


async def logout_post(request: web.Request, ) -> web.Response:
    """Log out

    Log out by deleting your token off the server.


    """
    return web.Response(status=200)
