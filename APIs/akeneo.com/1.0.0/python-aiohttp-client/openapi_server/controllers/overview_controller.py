from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_endpoints200_response import GetEndpoints200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_endpoints(request: web.Request, ) -> web.Response:
    """Get list of all endpoints

    This endpoint allows you to get the list of all the available endpoints. No need to be authenticated to use this endpoint.


    """
    return web.Response(status=200)
