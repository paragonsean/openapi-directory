from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_project(request: web.Request, ) -> web.Response:
    """Get metadata about the current project

    Returns project data for API key


    """
    return web.Response(status=200)
