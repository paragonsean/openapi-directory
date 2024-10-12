from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_listing_response import GetListingResponse
from openapi_server.models.get_listings_response import GetListingsResponse
from openapi_server import util


async def listings_all(request: web.Request, ecosystem_id, cursor=None, limit=None, external_id=None) -> web.Response:
    """List listings

    List listings

    :param ecosystem_id: 
    :type ecosystem_id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of records to return
    :type limit: int
    :param external_id: Filter on external_id
    :type external_id: str

    """
    return web.Response(status=200)


async def listings_one(request: web.Request, ecosystem_id, id) -> web.Response:
    """Get listing

    Get listing

    :param ecosystem_id: 
    :type ecosystem_id: str
    :param id: ID of the record you are acting upon.
    :type id: str

    """
    return web.Response(status=200)
