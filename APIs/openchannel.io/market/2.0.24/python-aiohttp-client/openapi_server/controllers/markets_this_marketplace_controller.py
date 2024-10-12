from typing import List, Dict
from aiohttp import web

from openapi_server.models.market import Market
from openapi_server import util


async def markets_this_get(request: web.Request, ) -> web.Response:
    """Returns the current marketplace

    


    """
    return web.Response(status=200)
