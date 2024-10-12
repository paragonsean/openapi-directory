from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def root_get(request: web.Request, url) -> web.Response:
    """Blocks images with nudity

    

    :param url: 
    :type url: str

    """
    return web.Response(status=200)
