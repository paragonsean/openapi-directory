from typing import List, Dict
from aiohttp import web

from openapi_server.models.servicepack import Servicepack
from openapi_server import util


async def servicepacks(request: web.Request, ) -> web.Response:
    """Overview of service packs

    


    """
    return web.Response(status=200)
