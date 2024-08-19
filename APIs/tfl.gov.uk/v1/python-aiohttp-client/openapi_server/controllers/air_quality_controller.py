from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def air_quality_get(request: web.Request, ) -> web.Response:
    """Gets air quality data feed

    


    """
    return web.Response(status=200)
