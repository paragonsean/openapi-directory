from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit_user_alt1_request import EditUserAlt1Request
from openapi_server.models.user import User
from openapi_server import util


async def edit_user(request: web.Request, user_id, body=None) -> web.Response:
    """Edit a user

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditUserAlt1Request.from_dict(body)
    return web.Response(status=200)


async def edit_user_alt1(request: web.Request, body=None) -> web.Response:
    """Edit a user

    

    :param body: 
    :type body: dict | bytes

    """
    body = EditUserAlt1Request.from_dict(body)
    return web.Response(status=200)


async def get_user(request: web.Request, user_id) -> web.Response:
    """Get a user

    

    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_user_alt1(request: web.Request, ) -> web.Response:
    """Get a user

    


    """
    return web.Response(status=200)
