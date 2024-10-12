from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.me import Me
from openapi_server import util


async def me_get(request: web.Request, ) -> web.Response:
    """Get token details

    


    """
    return web.Response(status=200)
