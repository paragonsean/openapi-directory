from typing import List, Dict
from aiohttp import web

from openapi_server.models.landing import Landing
from openapi_server import util


async def home_get(request: web.Request, ) -> web.Response:
    """Get top level links for this PI System Web API instance.

    


    """
    return web.Response(status=200)
