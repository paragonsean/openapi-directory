from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_doc(request: web.Request, ) -> web.Response:
    """Get swagger documentation

    


    """
    return web.Response(status=200)
