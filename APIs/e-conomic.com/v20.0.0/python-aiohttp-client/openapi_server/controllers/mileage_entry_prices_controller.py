from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.mileage_prices import MileagePrices
from openapi_server.models.mileage_prices_cursor_results import MileagePricesCursorResults
from openapi_server import util


async def get_all_mileage_entry_prices(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Mileage entry prices

    Use this endpoint to retrieve all Mileage entry prices in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_mileage_prices_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Mileage entry prices

    Use this endpoint to load a single Mileage entry prices by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_page_of_mileage_entry_prices(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Mileage entry prices

    Use this endpoint to load a page of Mileage entry prices.

    :param filter: 
    :type filter: str
    :param sort: 
    :type sort: str
    :param page_size: 
    :type page_size: int
    :param skip_pages: 
    :type skip_pages: int

    """
    return web.Response(status=200)
