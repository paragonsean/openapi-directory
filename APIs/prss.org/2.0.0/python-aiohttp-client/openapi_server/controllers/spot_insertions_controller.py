from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.spot_insertion import SpotInsertion
from openapi_server import util


async def api_v2_spotinsertions_get(request: web.Request, page_start=None, page_size=None, order_by_id=None) -> web.Response:
    """Returns the spot insertions matching the query parameters.

    

    :param page_start: The start page of the results to return. The first item is indexed at 0.
    :type page_start: int
    :param page_size: The number of items to return. Must be between 0 and 500, inclusive.
    :type page_size: int
    :param order_by_id: The sort order of the list of spot insertions, based on ID. If unspecified, the spot insertions are returned in random order. If using paging to iterate through the results, sort order should be specified.
    :type order_by_id: str

    """
    return web.Response(status=200)


async def api_v2_spotinsertions_id_delete(request: web.Request, id) -> web.Response:
    """Deletes the spot insertion with the given ID.

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_spotinsertions_id_get(request: web.Request, id) -> web.Response:
    """Returns the spot insertion matching the given ID.

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def api_v2_spotinsertions_post(request: web.Request, body=None) -> web.Response:
    """Creates a new spot insertion.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SpotInsertion.from_dict(body)
    return web.Response(status=200)
