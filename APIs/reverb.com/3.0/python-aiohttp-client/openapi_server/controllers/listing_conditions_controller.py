from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def listing_conditions_get(request: web.Request, ) -> web.Response:
    """List of supported product conditions

    List of supported product conditions


    """
    return web.Response(status=200)
