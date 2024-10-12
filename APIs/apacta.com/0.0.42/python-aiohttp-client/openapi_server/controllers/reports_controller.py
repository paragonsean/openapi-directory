from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def reports_get(request: web.Request, ) -> web.Response:
    """

    View list of report types


    """
    return web.Response(status=200)
