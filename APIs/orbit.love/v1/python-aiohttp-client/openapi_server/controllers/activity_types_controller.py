from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def workspace_slug_activity_types_get(request: web.Request, workspace_slug) -> web.Response:
    """List all activity types for a workspace

    

    :param workspace_slug: 
    :type workspace_slug: str

    """
    return web.Response(status=200)
