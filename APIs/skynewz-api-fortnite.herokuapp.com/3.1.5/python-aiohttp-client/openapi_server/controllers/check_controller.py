from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_get200_response import CheckGet200Response
from openapi_server.models.check_get_default_response import CheckGetDefaultResponse
from openapi_server import util


async def check_get(request: web.Request, ) -> web.Response:
    """Get Fortnite game status

    


    """
    return web.Response(status=200)
