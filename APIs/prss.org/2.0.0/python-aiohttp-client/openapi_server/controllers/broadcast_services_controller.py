from typing import List, Dict
from aiohttp import web

from openapi_server.models.broadcast_service import BroadcastService
from openapi_server.models.episode import Episode
from openapi_server.models.error import Error
from openapi_server import util


async def api_v2_broadcastservices_get(request: web.Request, page_start=None, page_size=None, order_by_id=None) -> web.Response:
    """Gets broadcast services matching the given criteria.

    

    :param page_start: The start page of the results to return. The first item is indexed at 0.
    :type page_start: int
    :param page_size: The number of items to return. Must be between 0 and 500, inclusive.
    :type page_size: int
    :param order_by_id: The sort order of the list of broadcast services, based on broadcast service ID. If unspecified, the broadcast services are returned in random order. If using paging to iterate through the results, sort order should be specified.
    :type order_by_id: str

    """
    return web.Response(status=200)


async def api_v2_broadcastservices_id_get(request: web.Request, id) -> web.Response:
    """Returns the broadcast service matching the given ID.

    

    :param id: The ID of the broadcast service to find.
    :type id: int

    """
    return web.Response(status=200)
