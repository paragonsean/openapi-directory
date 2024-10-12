from typing import List, Dict
from aiohttp import web

from openapi_server.models.currencies_response import CurrenciesResponse
from openapi_server.models.currency_response import CurrencyResponse
from openapi_server import util


async def currencies_get(request: web.Request, page_number=None, page_size=None, filter_search=None, filter_code_iso_alpha3=None, filter_code_iso_numeric3=None, filter_code_estandards_alpha=None, filter_currency_type=None, filter_category=None, sort=None) -> web.Response:
    """List of currencies

    Returns all available currencies. 

    :param page_number: Current page number.
    :type page_number: int
    :param page_size: Page size.&lt;br&gt;*Default value: 100* 
    :type page_size: int
    :param filter_search: Full text search with name, code, type, code_iso_alpha3, code_jsons_alpha, code_estandards_alpha, category.
    :type filter_search: str
    :param filter_code_iso_alpha3: Filtering by ISO code.
    :type filter_code_iso_alpha3: str
    :param filter_code_iso_numeric3: Filtering by ISO number.
    :type filter_code_iso_numeric3: int
    :param filter_code_estandards_alpha: Filtering by estandards code.
    :type filter_code_estandards_alpha: str
    :param filter_currency_type: Filtration by currency type.
    :type filter_currency_type: List[str]
    :param filter_category: Filtration by category.
    :type filter_category: List[str]
    :param sort: Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | type | -type | | category | -category | | code | -code | | code_iso_alpha3 | -code_iso_alpha3 | | code_iso_numeric3 | -code_iso_numeric3 | | code_estandards_alpha | -code_estandards_alpha | 
    :type sort: List[str]

    """
    return web.Response(status=200)


async def currencies_id_get(request: web.Request, id) -> web.Response:
    """Currency by ID

    Returns currency with specific ID. 

    :param id: Unique ID.
    :type id: str

    """
    return web.Response(status=200)
