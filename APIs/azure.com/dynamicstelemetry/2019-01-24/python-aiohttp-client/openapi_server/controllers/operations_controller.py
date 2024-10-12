from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation import Operation
from openapi_server import util


async def operations_list(request: web.Request, ) -> web.Response:
    """operations_list

    


    """
    return web.Response(status=200)
