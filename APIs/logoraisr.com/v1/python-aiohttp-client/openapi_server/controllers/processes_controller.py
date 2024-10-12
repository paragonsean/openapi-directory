from typing import List, Dict
from aiohttp import web

from openapi_server.models.process import Process
from openapi_server import util


async def processes_list(request: web.Request, ) -> web.Response:
    """Get process list.

    This GET-Method lists all on logoraisr available processes.


    """
    return web.Response(status=200)
