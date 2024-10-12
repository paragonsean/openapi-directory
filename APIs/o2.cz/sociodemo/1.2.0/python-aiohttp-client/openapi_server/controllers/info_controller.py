from typing import List, Dict
from aiohttp import web

from openapi_server.models.info_result import InfoResult
from openapi_server import util


async def get_info(request: web.Request, ) -> web.Response:
    """Information about versions of application and data.

    


    """
    return web.Response(status=200)
