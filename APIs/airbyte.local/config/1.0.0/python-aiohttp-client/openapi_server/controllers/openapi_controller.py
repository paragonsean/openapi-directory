from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_open_api_spec(request: web.Request, ) -> web.Response:
    """Returns the openapi specification

    


    """
    return web.Response(status=200)
