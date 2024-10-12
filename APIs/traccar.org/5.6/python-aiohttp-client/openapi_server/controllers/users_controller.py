from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server import util


async def users_get(request: web.Request, user_id=None) -> web.Response:
    """Fetch a list of Users

    

    :param user_id: Can only be used by admin or manager users
    :type user_id: str

    """
    return web.Response(status=200)


async def users_id_delete(request: web.Request, id) -> web.Response:
    """Delete a User

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def users_id_put(request: web.Request, id, body) -> web.Response:
    """Update a User

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = User.from_dict(body)
    return web.Response(status=200)


async def users_post(request: web.Request, body) -> web.Response:
    """Create a User

    

    :param body: 
    :type body: dict | bytes

    """
    body = User.from_dict(body)
    return web.Response(status=200)
