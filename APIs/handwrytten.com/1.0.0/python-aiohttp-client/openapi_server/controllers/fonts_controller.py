from typing import List, Dict
from aiohttp import web

from openapi_server.models.font import Font
from openapi_server import util


async def fonts_list(request: web.Request, ) -> web.Response:
    """Lists Handwryting styles available for use

    


    """
    return web.Response(status=200)
