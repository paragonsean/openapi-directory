from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_dto_paged_result import CustomerDtoPagedResult
from openapi_server.models.customer_location_item_dto import CustomerLocationItemDto
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def customers_get_customer_location_list_customer_idlocations(request: web.Request, customer_id) -> web.Response:
    """Gets a list of locations for the specified customer

    Sample rquest:                GET /customers/10000/locations

    :param customer_id: The customer id (CustomerCd) to retrieve locations for
    :type customer_id: str

    """
    return web.Response(status=200)


async def customers_get_list(request: web.Request, filter=None, page_size=None, page_index=None) -> web.Response:
    """Gets a list of customers

    Sample request:                GET /customers?filter&#x3D;visma&amp;pageSize&#x3D;10

    :param filter: An optional text string to find customers matching (searching fields id, name, gln, tax registration id). If not specified all customers are returned.
    :type filter: str
    :param page_size: The number of customers retrieved per page. If not specified, the default value of 100 will be used.
    :type page_size: int
    :param page_index: The zero based page index to retrieve
    :type page_index: int

    """
    return web.Response(status=200)
