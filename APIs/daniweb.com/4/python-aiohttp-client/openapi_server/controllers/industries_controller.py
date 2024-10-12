from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_get_industries import EndpointGetIndustries
from openapi_server import util


async def industries_get(request: web.Request, ) -> web.Response:
    """industries_get

    


    """
    return web.Response(status=200)
