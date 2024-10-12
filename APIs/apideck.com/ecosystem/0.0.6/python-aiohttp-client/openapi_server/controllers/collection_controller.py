from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_collection_response import GetCollectionResponse
from openapi_server.models.get_collections_response import GetCollectionsResponse
from openapi_server.models.get_listings_response import GetListingsResponse
from openapi_server import util


async def collection_listings_all(request: web.Request, ecosystem_id, id, cursor=None, limit=None) -> web.Response:
    """List collection listings

    List collection listings

    :param ecosystem_id: 
    :type ecosystem_id: str
    :param id: ID of the record you are acting upon.
    :type id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of records to return
    :type limit: int

    """
    return web.Response(status=200)


async def collections_all(request: web.Request, ecosystem_id, cursor=None, limit=None) -> web.Response:
    """List collections

    List collections

    :param ecosystem_id: 
    :type ecosystem_id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of records to return
    :type limit: int

    """
    return web.Response(status=200)


async def collections_one(request: web.Request, ecosystem_id, id) -> web.Response:
    """Get collection

    Get collection

    :param ecosystem_id: 
    :type ecosystem_id: str
    :param id: ID of the record you are acting upon.
    :type id: str

    """
    return web.Response(status=200)
