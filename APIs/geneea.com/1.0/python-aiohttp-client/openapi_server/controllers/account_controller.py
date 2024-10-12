from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_info(request: web.Request, ) -> web.Response:
    """Information about current user account

    getInfo


    """
    return web.Response(status=200)
