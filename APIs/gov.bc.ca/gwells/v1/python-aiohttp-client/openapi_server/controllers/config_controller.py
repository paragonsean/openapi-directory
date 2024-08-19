from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def config_list(request: web.Request, ) -> web.Response:
    """config_list

    serves general configuration


    """
    return web.Response(status=200)
