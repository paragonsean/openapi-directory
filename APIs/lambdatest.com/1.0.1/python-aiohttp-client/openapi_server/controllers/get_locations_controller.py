from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.locations import Locations
from openapi_server import util


async def locations(request: web.Request, ) -> web.Response:
    """Fetch Locations

    Fetch list of available Geolocations


    """
    return web.Response(status=200)
