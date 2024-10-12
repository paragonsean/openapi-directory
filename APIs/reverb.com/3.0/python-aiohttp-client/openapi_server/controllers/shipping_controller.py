from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def shipping_providers_get(request: web.Request, ) -> web.Response:
    """List of supported shipping providers

    List of supported shipping providers


    """
    return web.Response(status=200)


async def shipping_regions_get(request: web.Request, ) -> web.Response:
    """shipping_regions_get

    


    """
    return web.Response(status=200)
