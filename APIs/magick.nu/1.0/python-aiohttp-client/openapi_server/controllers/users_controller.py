from typing import List, Dict
from aiohttp import web

from openapi_server.models.password_dto import PasswordDTO
from openapi_server.models.user_dto import UserDTO
from openapi_server import util


async def get_users_email_email(request: web.Request, email) -> web.Response:
    """Check if email is available

    

    :param email: 
    :type email: str

    """
    return web.Response(status=200)


async def get_users_username_username(request: web.Request, username) -> web.Response:
    """Check if username is available

    

    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def post_users(request: web.Request, body) -> web.Response:
    """Create a new Tradeworks User

    

    :param body: 
    :type body: dict | bytes

    """
    body = UserDTO.from_dict(body)
    return web.Response(status=200)


async def put_users_password_username(request: web.Request, username, body) -> web.Response:
    """Update user&#39;s password

    

    :param username: 
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = PasswordDTO.from_dict(body)
    return web.Response(status=200)
