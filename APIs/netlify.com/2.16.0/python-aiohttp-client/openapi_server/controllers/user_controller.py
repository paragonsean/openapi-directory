from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.user import User
from openapi_server import util


async def get_current_user(request: web.Request, ) -> web.Response:
    """get_current_user

    


    """
    return web.Response(status=200)
