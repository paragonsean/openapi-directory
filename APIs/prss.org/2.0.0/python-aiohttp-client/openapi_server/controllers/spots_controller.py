from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.spot import Spot
from openapi_server import util


async def api_v2_spots_get(request: web.Request, page_start=None, page_size=None, order_by_id=None) -> web.Response:
    """Returns the spots matching the query parameters.

    

    :param page_start: The start page of the spot to return. The first item is indexed at 0.
    :type page_start: int
    :param page_size: The number of items to return. Must be between 0 and 500, inclusive.
    :type page_size: int
    :param order_by_id: The sort order of the list of spots, based on spot ID. If unspecified, the spots are returned in random order. If using paging to iterate through the results, sort order should be specified.
    :type order_by_id: str

    """
    return web.Response(status=200)


async def api_v2_spots_id_delete(request: web.Request, id) -> web.Response:
    """Deletes the spot with the given ID.

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_spots_id_get(request: web.Request, id) -> web.Response:
    """Returns the spot matching the given ID.

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_spots_post(request: web.Request, cd_drive_uri, name, notes) -> web.Response:
    """Creates a new spot.

    

    :param cd_drive_uri: The URI to the spot content in CD Drive. Format should be &#39;cddrive:id:{value}&#39; or &#39;cddrive://{path}&#39;.
    :type cd_drive_uri: str
    :param name: The name of the spot to create/update.
    :type name: str
    :param notes: Notes pertaining to the spot.
    :type notes: str

    """
    return web.Response(status=200)
