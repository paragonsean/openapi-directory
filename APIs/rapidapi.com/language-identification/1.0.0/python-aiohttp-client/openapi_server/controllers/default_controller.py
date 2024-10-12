from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def recognize_language_post(request: web.Request, x_rapid_api_host, x_rapid_api_key, text) -> web.Response:
    """Recognize Language

    

    :param x_rapid_api_host: 
    :type x_rapid_api_host: str
    :param x_rapid_api_key: 
    :type x_rapid_api_key: str
    :param text: text
    :type text: str

    """
    return web.Response(status=200)
