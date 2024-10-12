from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_category_type_dto import PageResultCategoryTypeDto
from openapi_server import util


async def category_types_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Category Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)
