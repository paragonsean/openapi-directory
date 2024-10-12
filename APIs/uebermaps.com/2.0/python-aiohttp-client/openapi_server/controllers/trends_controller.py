from typing import List, Dict
from aiohttp import web

from openapi_server.models.map import Map
from openapi_server import util


async def trends_latest_get(request: web.Request, ) -> web.Response:
    """List latest maps

    List latest maps.


    """
    return web.Response(status=200)


async def trends_recommended_get(request: web.Request, ) -> web.Response:
    """List recommended maps

    List recommended maps.


    """
    return web.Response(status=200)
