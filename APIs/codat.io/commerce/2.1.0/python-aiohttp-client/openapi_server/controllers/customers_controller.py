from typing import List, Dict
from aiohttp import web

from openapi_server.models.customers import Customers
from openapi_server import util


async def list_customers(request: web.Request, page, page_size=None, query=None, order_by=None) -> web.Response:
    """List customers

    List all commerce customers for the given company and data connection

    :param page: Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page: int
    :param page_size: Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    :type page_size: int
    :param query: Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    :type query: str
    :param order_by: Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    :type order_by: str

    """
    return web.Response(status=200)
