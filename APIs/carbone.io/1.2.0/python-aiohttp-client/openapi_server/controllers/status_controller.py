from typing import List, Dict
from aiohttp import web

from openapi_server.models.status_get200_response import StatusGet200Response
from openapi_server import util


async def status_get(request: web.Request, ) -> web.Response:
    """Fetch the API status and version

    


    """
    return web.Response(status=200)
