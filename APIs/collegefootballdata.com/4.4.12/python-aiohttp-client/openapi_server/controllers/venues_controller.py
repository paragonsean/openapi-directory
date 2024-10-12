from typing import List, Dict
from aiohttp import web

from openapi_server.models.venue import Venue
from openapi_server import util


async def get_venues(request: web.Request, ) -> web.Response:
    """Arena and venue information

    Venues


    """
    return web.Response(status=200)
