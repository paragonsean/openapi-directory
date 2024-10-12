from typing import List, Dict
from aiohttp import web

from openapi_server.models.root200_response import Root200Response
from openapi_server import util


async def root(request: web.Request, ) -> web.Response:
    """Root

    Returns a welcome message.


    """
    return web.Response(status=200)


async def spec(request: web.Request, ) -> web.Response:
    """Get JSON schema

    Gets the schema for the JSON API as a yaml file.


    """
    return web.Response(status=200)
