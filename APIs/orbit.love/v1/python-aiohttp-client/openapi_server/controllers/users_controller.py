from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def user_get(request: web.Request, ) -> web.Response:
    """Get info about the current user

    


    """
    return web.Response(status=200)
