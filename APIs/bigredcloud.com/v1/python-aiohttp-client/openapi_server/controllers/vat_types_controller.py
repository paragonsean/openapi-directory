from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_vat_type_dto import PageResultVatTypeDto
from openapi_server import util


async def vat_types_get(request: web.Request, ) -> web.Response:
    """Returns a list of global Vat Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)
