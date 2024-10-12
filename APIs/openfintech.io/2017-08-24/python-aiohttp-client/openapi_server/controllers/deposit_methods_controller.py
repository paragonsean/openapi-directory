from typing import List, Dict
from aiohttp import web

from openapi_server.models.deposit_method_response import DepositMethodResponse
from openapi_server.models.deposit_methods_response import DepositMethodsResponse
from openapi_server import util


async def deposit_methods_get(request: web.Request, page_number=None, page_size=None, filter_search=None, filter_name=None, filter_code=None, filter_processor_name=None, filter_category=None, sort=None) -> web.Response:
    """List of deposit methods

    Returns list of deposit methods. Each object contains information about deposit method such as name and category, also related link to deposit method issuer (which processing it). 

    :param page_number: Current page number.
    :type page_number: int
    :param page_size: Page size.&lt;br&gt;*Default value: 100* 
    :type page_size: int
    :param filter_search: Full text search with id, name, code, category.
    :type filter_search: str
    :param filter_name: Filtering by name.
    :type filter_name: str
    :param filter_code: Filtering by code.
    :type filter_code: str
    :param filter_processor_name: Filtering by processor_name.
    :type filter_processor_name: str
    :param filter_category: Filtering by category.
    :type filter_category: List[str]
    :param sort: Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | | processor_name | -processor_name | | category | -category | 
    :type sort: List[str]

    """
    return web.Response(status=200)


async def deposit_methods_id_get(request: web.Request, id) -> web.Response:
    """Deposit method by ID

    Returns deposit method with specific ID. 

    :param id: Unique ID.
    :type id: str

    """
    return web.Response(status=200)
