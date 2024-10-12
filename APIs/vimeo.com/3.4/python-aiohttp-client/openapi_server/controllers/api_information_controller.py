from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint import Endpoint
from openapi_server import util


async def get_endpoints(request: web.Request, openapi=None) -> web.Response:
    """Get an API specification

    

    :param openapi: Return an OpenAPI specification.
    :type openapi: bool

    """
    return web.Response(status=200)
