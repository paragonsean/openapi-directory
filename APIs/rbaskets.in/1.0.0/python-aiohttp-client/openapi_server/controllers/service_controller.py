from typing import List, Dict
from aiohttp import web

from openapi_server.models.version import Version
from openapi_server import util


async def api_version_get(request: web.Request, ) -> web.Response:
    """Get service version

    Get service version.


    """
    return web.Response(status=200)
