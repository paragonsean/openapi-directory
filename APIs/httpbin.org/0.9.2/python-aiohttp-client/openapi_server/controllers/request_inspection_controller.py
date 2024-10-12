from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def headers_get(request: web.Request, ) -> web.Response:
    """Return the incoming request&#39;s HTTP headers.

    


    """
    return web.Response(status=200)


async def ip_get(request: web.Request, ) -> web.Response:
    """Returns the requester&#39;s IP Address.

    


    """
    return web.Response(status=200)


async def user_agent_get(request: web.Request, ) -> web.Response:
    """Return the incoming requests&#39;s User-Agent header.

    


    """
    return web.Response(status=200)
