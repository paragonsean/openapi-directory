from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def numbers_nod_get(request: web.Request, ) -> web.Response:
    """numbers_nod_get

    Get the number of the day for current day


    """
    return web.Response(status=200)
