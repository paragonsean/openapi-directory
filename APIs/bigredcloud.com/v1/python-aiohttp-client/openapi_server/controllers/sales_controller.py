from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_sales_query_dto import PageResultSalesQueryDto
from openapi_server import util


async def sales_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Sales Entries, Sales Invoices and Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)
