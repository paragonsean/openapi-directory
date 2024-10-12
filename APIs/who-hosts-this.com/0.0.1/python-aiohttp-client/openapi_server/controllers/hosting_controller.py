from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def detect_get(request: web.Request, url) -> web.Response:
    """Discover the hosting provider for a web site

    

    :param url: The url of the page to check
    :type url: str

    """
    return web.Response(status=200)
