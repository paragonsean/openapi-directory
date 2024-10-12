from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def eula_accept(request: web.Request, ) -> web.Response:
    """Accepts the EULA

    


    """
    return web.Response(status=200)
