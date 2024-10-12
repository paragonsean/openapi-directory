from typing import List, Dict
from aiohttp import web

from openapi_server.models.laying_body_resource_collection import LayingBodyResourceCollection
from openapi_server import util


async def get_laying_bodies(request: web.Request, ) -> web.Response:
    """Returns all laying bodies.

    


    """
    return web.Response(status=200)
