from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_vat_rate_dto import PageResultVatRateDto
from openapi_server import util


async def vat_rates_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Vat Rates. Supports OData querying protocol.  Filtering is allowed by \&quot;vatCategoryId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields.

    


    """
    return web.Response(status=200)
