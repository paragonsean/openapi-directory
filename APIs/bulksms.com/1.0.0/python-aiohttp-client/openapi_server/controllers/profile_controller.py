from typing import List, Dict
from aiohttp import web

from openapi_server.models.profile import Profile
from openapi_server import util


async def profile_get(request: web.Request, ) -> web.Response:
    """Get profile

    Returns information about your user profile


    """
    return web.Response(status=200)
