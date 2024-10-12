from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server import util


async def get_user(request: web.Request, user_id) -> web.Response:
    """Returns details of a specific fire.com user.

    You can retrieve the details of a specific fire.com user

    :param user_id: 
    :type user_id: int

    """
    return web.Response(status=200)


async def get_users(request: web.Request, ) -> web.Response:
    """Returns list of all users on your fire.com account

    You can retrieve the details of all fire.com users on your acount.


    """
    return web.Response(status=200)
