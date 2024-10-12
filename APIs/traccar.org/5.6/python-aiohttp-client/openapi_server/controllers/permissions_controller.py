from typing import List, Dict
from aiohttp import web

from openapi_server.models.permission import Permission
from openapi_server import util


async def permissions_delete(request: web.Request, body) -> web.Response:
    """Unlink an Object from another Object

    

    :param body: 
    :type body: dict | bytes

    """
    body = Permission.from_dict(body)
    return web.Response(status=200)


async def permissions_post(request: web.Request, body) -> web.Response:
    """Link an Object to another Object

    

    :param body: 
    :type body: dict | bytes

    """
    body = Permission.from_dict(body)
    return web.Response(status=200)
