from typing import List, Dict
from aiohttp import web

from openapi_server.models.branding_options import BrandingOptions
from openapi_server import util


async def get_branding_css(request: web.Request, ) -> web.Response:
    """Gets branding css.

    


    """
    return web.Response(status=200)


async def get_branding_css2(request: web.Request, ) -> web.Response:
    """Gets branding css.

    


    """
    return web.Response(status=200)


async def get_branding_options(request: web.Request, ) -> web.Response:
    """Gets branding configuration.

    


    """
    return web.Response(status=200)
