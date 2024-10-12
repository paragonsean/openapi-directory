from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.introspection import Introspection
from openapi_server.models.introspection_v2 import IntrospectionV2
from openapi_server import util


async def get_auth_introspect(request: web.Request, ) -> web.Response:
    """Performs introspection of the provided Bearer JWT token

    


    """
    return web.Response(status=200)


async def get_auth_introspect_v2(request: web.Request, ) -> web.Response:
    """Performs introspection of the provided Bearer JWT token

    


    """
    return web.Response(status=200)
