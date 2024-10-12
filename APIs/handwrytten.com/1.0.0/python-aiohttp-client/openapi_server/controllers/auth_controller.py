from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_password200_response import ChangePassword200Response
from openapi_server.models.change_password_request import ChangePasswordRequest
from openapi_server.models.login import Login
from openapi_server.models.login200_response import Login200Response
from openapi_server.models.logout_request import LogoutRequest
from openapi_server.models.register200_response import Register200Response
from openapi_server.models.registration import Registration
from openapi_server.models.reset_password_request_request import ResetPasswordRequestRequest
from openapi_server import util


async def change_password(request: web.Request, body) -> web.Response:
    """changes a user&#39;s password

    

    :param body: Change password
    :type body: dict | bytes

    """
    body = ChangePasswordRequest.from_dict(body)
    return web.Response(status=200)


async def login(request: web.Request, body) -> web.Response:
    """Logs in to an existing account

    

    :param body: Login to account
    :type body: dict | bytes

    """
    body = Login.from_dict(body)
    return web.Response(status=200)


async def logout(request: web.Request, body) -> web.Response:
    """logs out a session uid

    

    :param body: logout session
    :type body: dict | bytes

    """
    body = LogoutRequest.from_dict(body)
    return web.Response(status=200)


async def register(request: web.Request, body) -> web.Response:
    """Registers a new account

    

    :param body: New user account information
    :type body: dict | bytes

    """
    body = Registration.from_dict(body)
    return web.Response(status=200)


async def reset_password_request(request: web.Request, body) -> web.Response:
    """resets a user&#39;s password

    

    :param body: Reset password
    :type body: dict | bytes

    """
    body = ResetPasswordRequestRequest.from_dict(body)
    return web.Response(status=200)
