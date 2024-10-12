from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_route_types_response import V3RouteTypesResponse
from openapi_server import util


async def route_types_get_route_types(request: web.Request, token=None, devid=None, signature=None) -> web.Response:
    """View all route types and their names

    

    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)
