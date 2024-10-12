from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_password import ChangePassword
from openapi_server.models.new_user import NewUser
from openapi_server import util


async def add_user(request: web.Request, authorization, body) -> web.Response:
    """add_user

    Add new user

    :param authorization: Authorization token (provided upon successful login)
    :type authorization: str
    :param body: Details of a new user including first name, last name, desired username and a password
    :type body: dict | bytes

    """
    body = NewUser.from_dict(body)
    return web.Response(status=200)


async def change_password(request: web.Request, authorization, body) -> web.Response:
    """change_password

    Change user password

    :param authorization: Authorization token (provided upon successful login)
    :type authorization: str
    :param body: Information about the user password to be changed including id and new password
    :type body: dict | bytes

    """
    body = ChangePassword.from_dict(body)
    return web.Response(status=200)
