from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_credentials import ApiCredentials
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.login_request import LoginRequest
from openapi_server.models.register_request import RegisterRequest
from openapi_server import util


async def login(request: web.Request, body) -> web.Response:
    """Login

    User Login - The login will give your tokens

    :param body: 
    :type body: dict | bytes

    """
    body = LoginRequest.from_dict(body)
    return web.Response(status=200)


async def lost_password(request: web.Request, body) -> web.Response:
    """Lost password

    Lost password - Your password will be regenerated and sent to your email

    :param body: Your email
    :type body: str

    """
    return web.Response(status=200)


async def register(request: web.Request, body) -> web.Response:
    """User Registration

    User Registration - Create a new user on BeezUP

    :param body: 
    :type body: dict | bytes

    """
    body = RegisterRequest.from_dict(body)
    return web.Response(status=200)
