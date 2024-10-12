from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def currencies_display_get(request: web.Request, ) -> web.Response:
    """List of supported display currencies for browsing listings

    List of supported display currencies for browsing listings


    """
    return web.Response(status=200)


async def currencies_listing_get(request: web.Request, ) -> web.Response:
    """List of supported listing currencies for shops

    List of supported listing currencies for shops


    """
    return web.Response(status=200)
