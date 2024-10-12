from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def users_usage_get(request: web.Request, ) -> web.Response:
    """Get API usuage details

    Returns API request consumption details.


    """
    return web.Response(status=200)
