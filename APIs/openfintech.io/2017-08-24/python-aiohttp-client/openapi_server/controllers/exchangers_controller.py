from typing import List, Dict
from aiohttp import web

from openapi_server.models.exchanger_response import ExchangerResponse
from openapi_server.models.exchangers_response import ExchangersResponse
from openapi_server import util


async def exchangers_get(request: web.Request, page_number=None, page_size=None, filter_name=None, filter_status=None, sort=None) -> web.Response:
    """List of exchangers

    Returns list of exchange markets. Each object contains general information about exchanger such as name and status, also information about rates export and related link to main organization.&lt;br&gt; Rates export standards is represented by: * [estandards](http://estandards.info) * [jsons](http://jsons.info) * ratex - our internal standard 

    :param page_number: Current page number.
    :type page_number: int
    :param page_size: Page size.&lt;br&gt;*Default value: 100* 
    :type page_size: int
    :param filter_name: Filtering by name.
    :type filter_name: str
    :param filter_status: Filtration by status.
    :type filter_status: List[str]
    :param sort: Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | status | -status | | wmid | -wmid | | rate_type | -rate_type | | rates_export_standard | &lt;nobr&gt;-rates_export_standard&lt;/nobr&gt; | 
    :type sort: List[str]

    """
    return web.Response(status=200)


async def exchangers_id_get(request: web.Request, id) -> web.Response:
    """Exchanger by ID

    Returns exchanger with specific ID. 

    :param id: Unique ID.
    :type id: str

    """
    return web.Response(status=200)
