from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_versions_versions_get(request: web.Request, ) -> web.Response:
    """Get Versions

    Respond with the text/csv representation for the served versions.


    """
    return web.Response(status=200)
