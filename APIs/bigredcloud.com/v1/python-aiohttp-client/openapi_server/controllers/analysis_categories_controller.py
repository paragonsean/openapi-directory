from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_analysis_category_dto import PageResultAnalysisCategoryDto
from openapi_server import util


async def analysis_categories_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s Analysis Categories. Supports OData querying protocol.  Filtering is allowed by \&quot;categoryTypeId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields.

    


    """
    return web.Response(status=200)
