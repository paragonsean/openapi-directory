from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.profiles import Profiles
from openapi_server import util


async def profiles(request: web.Request, ) -> web.Response:
    """Fetch login profiles

    Fetch login profiles


    """
    return web.Response(status=200)
