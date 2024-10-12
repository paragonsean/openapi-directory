from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server import util


async def user_delete(request: web.Request, ) -> web.Response:
    """Triggers user account deletion.

    


    """
    return web.Response(status=200)


async def user_get(request: web.Request, ) -> web.Response:
    """Gets the informations for the user.

    Gets the informations for the user.


    """
    return web.Response(status=200)
