from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.project_customer import ProjectCustomer
from openapi_server.models.project_customer_cursor_results import ProjectCustomerCursorResults
from openapi_server import util


async def get_all_project_customers(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Project Customers

    Use this endpoint to retrieve all Project Customers in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_number_of_project_customers(request: web.Request, filter=None) -> web.Response:
    """Retrieve the number of Project Customers

    Call this endpoint to get the number of Project Customers. You can use a filtering as well.

    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_page_of_project_customers(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Project Customers

    Use this endpoint to load a page of Project Customers.

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


async def get_project_customer_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Project Customer

    Use this endpoint to load a single Project Customer by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)
