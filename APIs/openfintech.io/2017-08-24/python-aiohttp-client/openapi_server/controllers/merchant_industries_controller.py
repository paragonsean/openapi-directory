from typing import List, Dict
from aiohttp import web

from openapi_server.models.merchant_industries_response import MerchantIndustriesResponse
from openapi_server.models.merchant_industry_response import MerchantIndustryResponse
from openapi_server import util


async def merchant_industries_get(request: web.Request, page_number=None, page_size=None, filter_name=None) -> web.Response:
    """List of merchant industries

    Returns all available merchant fields of activity. 

    :param page_number: Current page number.
    :type page_number: int
    :param page_size: Page size.&lt;br&gt;*Default value: 100* 
    :type page_size: int
    :param filter_name: Filtering by name.
    :type filter_name: str

    """
    return web.Response(status=200)


async def merchant_industries_id_get(request: web.Request, id) -> web.Response:
    """Merchant industry by ID

    Returns merchant industry with specific ID. 

    :param id: Unique ID.
    :type id: str

    """
    return web.Response(status=200)
