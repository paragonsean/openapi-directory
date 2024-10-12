from typing import List, Dict
from aiohttp import web

from openapi_server.models.sub_user_data import SubUserData
from openapi_server import util


async def sub_user_delete(request: web.Request, id) -> web.Response:
    """Delete a subuser

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def sub_user_get(request: web.Request, id) -> web.Response:
    """Get a sub user. The user must be assigend to the user that makes this call.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def sub_user_post(request: web.Request, body) -> web.Response:
    """Creates or updates a subuser.              To create a new user set no ID (empty)

    

    :param body: 
    :type body: dict | bytes

    """
    body = SubUserData.from_dict(body)
    return web.Response(status=200)
