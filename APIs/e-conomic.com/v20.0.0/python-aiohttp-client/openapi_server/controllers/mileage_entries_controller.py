from typing import List, Dict
from aiohttp import web

from openapi_server.models.created_result import CreatedResult
from openapi_server.models.error import Error
from openapi_server.models.mileage import Mileage
from openapi_server.models.mileage_cursor_results import MileageCursorResults
from openapi_server.models.mileage_numbers_collection import MileageNumbersCollection
from openapi_server import util


async def approve_mileage_entries_0(request: web.Request, body=None) -> web.Response:
    """Approve a list of Mileage entries

    Use this endpoint to approve a list of Mileage entries.

    :param body: 
    :type body: dict | bytes

    """
    body = MileageNumbersCollection.from_dict(body)
    return web.Response(status=200)


async def create_mileage(request: web.Request, body=None) -> web.Response:
    """Create a single Mileage entry

    Use this endpoint to create a single Mileage entry.

    :param body: 
    :type body: dict | bytes

    """
    body = Mileage.from_dict(body)
    return web.Response(status=200)


async def delete_mileage_by_id(request: web.Request, number) -> web.Response:
    """Delete single Mileage entry

    Use this endpoint to delete a single Mileage entry by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_all_mileage_entries(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Mileage entries

    Use this endpoint to retrieve all Mileage entries in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_mileage_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Mileage entry

    Use this endpoint to load a single Mileage entry by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_number_of_mileage_entries(request: web.Request, filter=None) -> web.Response:
    """Retrieve the number of Mileage entries

    Call this endpoint to get the number of Mileage entries. You can use a filtering as well.

    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_page_of_mileage_entries(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Mileage entries

    Use this endpoint to load a page of Mileage entries.

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


async def update_mileage(request: web.Request, body=None) -> web.Response:
    """Update a single Mileage entry

    Use this endpoint to update a single Mileage entry.

    :param body: 
    :type body: dict | bytes

    """
    body = Mileage.from_dict(body)
    return web.Response(status=200)
