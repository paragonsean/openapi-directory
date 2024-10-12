from typing import List, Dict
from aiohttp import web

from openapi_server.models.media import Media
from openapi_server import util


async def media_post(request: web.Request, body) -> web.Response:
    """Submit a new media file

    

    :param body: Binary media file
    :type body: str

    """
    return web.Response(status=200)
