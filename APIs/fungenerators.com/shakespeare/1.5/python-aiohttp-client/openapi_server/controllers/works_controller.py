from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def shakespeare_quote_get(request: web.Request, ) -> web.Response:
    """shakespeare_quote_get

    Get a random Shakespeare quote.


    """
    return web.Response(status=200)
