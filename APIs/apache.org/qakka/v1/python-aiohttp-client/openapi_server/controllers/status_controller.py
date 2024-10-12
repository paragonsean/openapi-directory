from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def status(request: web.Request, ) -> web.Response:
    """Status of webapp.

    


    """
    return web.Response(status=200)
