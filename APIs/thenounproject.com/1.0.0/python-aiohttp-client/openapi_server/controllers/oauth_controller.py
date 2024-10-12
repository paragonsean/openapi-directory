from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_api_quota_status(request: web.Request, ) -> web.Response:
    """Get api quota status

    Returns current oauth usage and limits


    """
    return web.Response(status=200)
