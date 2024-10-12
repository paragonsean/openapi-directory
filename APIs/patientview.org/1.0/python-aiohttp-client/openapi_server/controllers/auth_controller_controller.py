from typing import List, Dict
from aiohttp import web

from openapi_server.models.credentials import Credentials
from openapi_server.models.user import User
from openapi_server.models.user_token import UserToken
from openapi_server import util


async def get_basic_user_information(request: web.Request, token) -> web.Response:
    """Get Basic User Information

    Once logged in and have a token, get basic user information including group role membership

    :param token: token
    :type token: str

    """
    return web.Response(status=200)


async def log_in(request: web.Request, body=None) -> web.Response:
    """Log In

    Authenticate using username and password, returns token, which must be added to X-Auth-Token in header of all future requests

    :param body: credentials
    :type body: dict | bytes

    """
    body = Credentials.from_dict(body)
    return web.Response(status=200)


async def log_out(request: web.Request, token) -> web.Response:
    """Log Out

    Log Out

    :param token: token
    :type token: str

    """
    return web.Response(status=200)
