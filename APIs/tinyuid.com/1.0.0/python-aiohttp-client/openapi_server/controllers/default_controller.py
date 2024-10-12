from typing import List, Dict
from aiohttp import web

from openapi_server.models.v1_shorten_post200_response import V1ShortenPost200Response
from openapi_server import util


async def v1_shorten_post(request: web.Request, url) -> web.Response:
    """Create short link

    

    :param url: Link
    :type url: str

    """
    return web.Response(status=200)
