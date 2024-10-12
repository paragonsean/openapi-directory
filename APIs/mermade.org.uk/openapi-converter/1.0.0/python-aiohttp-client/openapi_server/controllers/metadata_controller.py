from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_status(request: web.Request, ) -> web.Response:
    """Get the status of the API

    


    """
    return web.Response(status=200)
