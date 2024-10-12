from typing import List, Dict
from aiohttp import web

from openapi_server.models.spec import Spec
from openapi_server import util


async def specs(request: web.Request, ) -> web.Response:
    """Fetch Swagger information

    This operation shows the details of the Swagger specification. 


    """
    return web.Response(status=200)
