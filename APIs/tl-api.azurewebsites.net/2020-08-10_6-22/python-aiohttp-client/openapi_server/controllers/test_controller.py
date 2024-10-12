from typing import List, Dict
from aiohttp import web

from openapi_server.models.test_dto import TestDTO
from openapi_server import util


async def test_get(request: web.Request, ) -> web.Response:
    """Get the all Test objects.             

    


    """
    return web.Response(status=200)
