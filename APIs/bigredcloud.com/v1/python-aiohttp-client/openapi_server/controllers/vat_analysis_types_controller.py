from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_vat_analysis_type_dto import PageResultVatAnalysisTypeDto
from openapi_server import util


async def vat_analysis_types_get(request: web.Request, ) -> web.Response:
    """Returns a list of global Vat Analysis Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)
