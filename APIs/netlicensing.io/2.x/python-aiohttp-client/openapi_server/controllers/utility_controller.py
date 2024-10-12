from typing import List, Dict
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing
from openapi_server import util


async def license_types(request: web.Request, ) -> web.Response:
    """List License Types

    Return a list of all License Types supported by the service


    """
    return web.Response(status=200)


async def licensing_models(request: web.Request, ) -> web.Response:
    """List Licensing Models

    Return a list of all licensing models supported by the service


    """
    return web.Response(status=200)
