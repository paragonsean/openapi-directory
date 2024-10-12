from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def workspaces_get(request: web.Request, ) -> web.Response:
    """Get all workspaces for the current user

    


    """
    return web.Response(status=200)


async def workspaces_workspace_slug_get(request: web.Request, workspace_slug, include_orbit_level_counts=None) -> web.Response:
    """Get a workspace

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param include_orbit_level_counts: Include the number of members by Orbit Level in the attributes
    :type include_orbit_level_counts: bool

    """
    return web.Response(status=200)
