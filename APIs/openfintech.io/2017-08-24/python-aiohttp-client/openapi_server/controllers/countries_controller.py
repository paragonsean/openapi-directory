from typing import List, Dict
from aiohttp import web

from openapi_server.models.countries_response import CountriesResponse
from openapi_server.models.country_response import CountryResponse
from openapi_server import util


async def countries_get(request: web.Request, page_number=None, page_size=None, filter_region=None, filter_sub_region=None, sort=None) -> web.Response:
    """List of countries

    Returns all available countries. 

    :param page_number: Current page number.
    :type page_number: int
    :param page_size: Page size.&lt;br&gt;*Default value: 100* 
    :type page_size: int
    :param filter_region: Filtration by region.
    :type filter_region: List[str]
    :param filter_sub_region: Filtration by sub region.
    :type filter_sub_region: List[str]
    :param sort: Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | area | -area | | population | -population | | region | -region | | sub_region | -sub_region | 
    :type sort: List[str]

    """
    return web.Response(status=200)


async def countries_id_get(request: web.Request, id) -> web.Response:
    """Country by ID

    Returns country with specific ID. 

    :param id: Unique ID.
    :type id: str

    """
    return web.Response(status=200)
