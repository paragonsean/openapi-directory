from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_provider_response import PaymentProviderResponse
from openapi_server.models.payment_providers_response import PaymentProvidersResponse
from openapi_server import util


async def payment_providers_get(request: web.Request, page_number=None, page_size=None, filter_search=None, filter_name=None, filter_code=None, filter_types=None, filter_sales_channels=None, filter_features=None, sort=None) -> web.Response:
    """List of payment providers

    A payment service provider (PSP) offers shops online services for accepting electronic payments by a variety of payment methods.&lt;br&gt; Endpoint returns list of PSPs. Each object contains: name, type, supported features and sales channels, also related link to available payment methods and main organization. 

    :param page_number: Current page number.
    :type page_number: int
    :param page_size: Page size.&lt;br&gt;*Default value: 100* 
    :type page_size: int
    :param filter_search: Full text search with id, code, name.
    :type filter_search: str
    :param filter_name: Filtering by name.
    :type filter_name: str
    :param filter_code: Filtering by code.
    :type filter_code: str
    :param filter_types: Filtering by types.
    :type filter_types: List[str]
    :param filter_sales_channels: Filtering by sales channels.
    :type filter_sales_channels: List[str]
    :param filter_features: Filtering by features.
    :type filter_features: List[str]
    :param sort: Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | 
    :type sort: List[str]

    """
    return web.Response(status=200)


async def payment_providers_id_get(request: web.Request, id) -> web.Response:
    """Payment provider by ID

    Returns payment provider with specific ID. 

    :param id: Unique ID.
    :type id: str

    """
    return web.Response(status=200)
