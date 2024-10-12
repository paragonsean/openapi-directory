from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.get_providers200_response import GetProviders200Response
from openapi_server import util


async def get_providers(request: web.Request, ) -> web.Response:
    """List providers

    Get a list of providers.  *New in version 2.1.0* 


    """
    return web.Response(status=200)
