from typing import List, Dict
from aiohttp import web

from openapi_server.models.version_response import VersionResponse
from openapi_server import util


async def get_version(request: web.Request, ) -> web.Response:
    """Show version info

    Show version info


    """
    return web.Response(status=200)
