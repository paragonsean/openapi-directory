from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_venue import JsonVenue
from openapi_server import util


async def resource10_venue_venue_id_get_venue_get(request: web.Request, venue_id) -> web.Response:
    """Get a venue by its unique id.

    Get a venue by its unique id.

    :param venue_id: the venue&#39;s id
    :type venue_id: str

    """
    return web.Response(status=200)
