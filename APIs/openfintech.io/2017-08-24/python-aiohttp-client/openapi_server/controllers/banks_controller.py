from typing import List, Dict
from aiohttp import web

from openapi_server.models.bank_response import BankResponse
from openapi_server.models.banks_response import BanksResponse
from openapi_server import util


async def banks_get(request: web.Request, page_number=None, page_size=None, filter_sort_code=None, filter_code=None, filter_status=None, sort=None) -> web.Response:
    """List of banks

    Returns list of banks. Each object contains general information about bank such as name and status, also information about bank details and related link to main organization. 

    :param page_number: Current page number.
    :type page_number: int
    :param page_size: Page size.&lt;br&gt;*Default value: 100* 
    :type page_size: int
    :param filter_sort_code: Filtering by banks code.
    :type filter_sort_code: str
    :param filter_code: Filtering by code.
    :type filter_code: str
    :param filter_status: Filtration by status.
    :type filter_status: List[str]
    :param sort: Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | sort_code | -sort_code | 
    :type sort: List[str]

    """
    return web.Response(status=200)


async def banks_id_get(request: web.Request, id) -> web.Response:
    """Bank by ID

    Returns bank with specific ID. 

    :param id: Unique ID.
    :type id: str

    """
    return web.Response(status=200)
