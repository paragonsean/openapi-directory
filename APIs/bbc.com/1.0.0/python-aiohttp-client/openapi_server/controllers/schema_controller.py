from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def get_api(request: web.Request, ) -> web.Response:
    """Get API definition

    Get API definition


    """
    return web.Response(status=200)


async def get_xsd(request: web.Request, ) -> web.Response:
    """Get Schema definition

    Get Schema definition


    """
    return web.Response(status=200)
