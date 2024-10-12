from typing import List, Dict
from aiohttp import web

from openapi_server.models.login import Login
from openapi_server import util


async def check_login(request: web.Request, authorization) -> web.Response:
    """Check if any user is logged in

    If a user is loggedin the username will be returned

    :param authorization: Authorization token (provided upon successful login)
    :type authorization: str

    """
    return web.Response(status=200)


async def login(request: web.Request, body) -> web.Response:
    """Login method

    After a successful login a token is returned. This is a Bearer token. To authenticate with it use the Authorization header and set value to Bearer empty space and the token value.

    :param body: Username and password combination to allow users to log-in
    :type body: dict | bytes

    """
    body = Login.from_dict(body)
    return web.Response(status=200)
