from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_health(request: web.Request, ) -> web.Response:
    """Get health of Tune-in service (which includes its uptime).

    


    """
    return web.Response(status=200)
