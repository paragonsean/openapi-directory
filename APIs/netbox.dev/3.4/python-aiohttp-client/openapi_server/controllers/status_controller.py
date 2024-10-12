from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def status_list(request: web.Request, ) -> web.Response:
    """status_list

    A lightweight read-only endpoint for conveying NetBox&#39;s current operational status.


    """
    return web.Response(status=200)
