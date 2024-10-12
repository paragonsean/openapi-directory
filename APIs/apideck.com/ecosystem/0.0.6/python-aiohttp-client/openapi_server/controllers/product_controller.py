from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_listings_response import GetListingsResponse
from openapi_server.models.get_product_response import GetProductResponse
from openapi_server.models.get_products_response import GetProductsResponse
from openapi_server import util


async def product_listings_all(request: web.Request, ecosystem_id, id, cursor=None, limit=None) -> web.Response:
    """List product listings

    List product listings

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


async def products_all(request: web.Request, ecosystem_id) -> web.Response:
    """List products

    List products

    :param ecosystem_id: 
    :type ecosystem_id: str

    """
    return web.Response(status=200)


async def products_one(request: web.Request, ecosystem_id, id) -> web.Response:
    """Get product

    Get product

    :param ecosystem_id: 
    :type ecosystem_id: str
    :param id: ID of the record you are acting upon.
    :type id: str

    """
    return web.Response(status=200)
