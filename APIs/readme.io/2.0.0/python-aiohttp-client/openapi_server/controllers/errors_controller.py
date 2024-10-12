from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_errors(request: web.Request, ) -> web.Response:
    """Get errors

    Returns with all of the error page types for this project


    """
    return web.Response(status=200)
