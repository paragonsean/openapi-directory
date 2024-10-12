from typing import List, Dict
from aiohttp import web

from openapi_server.models.utc_time_response import UtcTimeResponse
from openapi_server import util


async def get_utc_time(request: web.Request, ) -> web.Response:
    """Gets the current UTC time.

    


    """
    return web.Response(status=200)
