from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def resources_json_get(request: web.Request, q) -> web.Response:
    """Get Resources by search query

    Global search

    :param q: The search query supplied by the user
    :type q: str

    """
    return web.Response(status=200)
