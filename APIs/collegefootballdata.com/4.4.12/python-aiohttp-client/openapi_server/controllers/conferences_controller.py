from typing import List, Dict
from aiohttp import web

from openapi_server.models.conference import Conference
from openapi_server import util


async def get_conferences(request: web.Request, ) -> web.Response:
    """Conferences

    Get conference list


    """
    return web.Response(status=200)
