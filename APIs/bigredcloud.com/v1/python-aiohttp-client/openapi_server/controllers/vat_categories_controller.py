from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_vat_category_dto import PageResultVatCategoryDto
from openapi_server.models.vat_rates_by_vat_category_dto import VatRatesByVatCategoryDto
from openapi_server import util


async def vat_categories_get(request: web.Request, ) -> web.Response:
    """Returns a list of global Vat Categories. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)


async def vat_categories_process_vat_rates(request: web.Request, body) -> web.Response:
    """Process Vat Rates

    

    :param body: Array of Vat Rates.
    :type body: list | bytes

    """
    body = [VatRatesByVatCategoryDto.from_dict(d) for d in body]
    return web.Response(status=200)
