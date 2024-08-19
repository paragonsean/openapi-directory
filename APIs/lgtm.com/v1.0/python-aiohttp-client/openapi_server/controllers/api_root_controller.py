from typing import List, Dict
from aiohttp import web

from openapi_server.models.version import Version
from openapi_server import util


async def get_spec(request: web.Request, ) -> web.Response:
    """API specification

    Get the specification of this API in [OpenAPI](https://github.com/OAI/OpenAPI-Specification) format. This endpoint does not require an access token. This makes it easier for you to use the specification with third-party tools.


    """
    return web.Response(status=200)


async def get_version(request: web.Request, ) -> web.Response:
    """Version information

    Get the version information of this API.


    """
    return web.Response(status=200)
