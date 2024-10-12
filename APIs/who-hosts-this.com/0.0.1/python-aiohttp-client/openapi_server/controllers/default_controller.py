from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def status_get(request: web.Request, ) -> web.Response:
    """View usage details for the current billing period

    


    """
    return web.Response(status=200)
