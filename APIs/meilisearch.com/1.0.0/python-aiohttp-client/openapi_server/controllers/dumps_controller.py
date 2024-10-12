from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def create_a_dump(request: web.Request, ) -> web.Response:
    """Create a dump

    Create a dump


    """
    return web.Response(status=200)
