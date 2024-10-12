from typing import List, Dict
from aiohttp import web

from openapi_server.models.groov_info import GroovInfo
from openapi_server import util


async def groov_info(request: web.Request, ) -> web.Response:
    """groov_info

    Get information about groov View. No authorization required.


    """
    return web.Response(status=200)
