from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_collection import JsonCollection
from openapi_server import util


async def get_index(request: web.Request, ) -> web.Response:
    """Show index.

    Show Service index.


    """
    return web.Response(status=200)
