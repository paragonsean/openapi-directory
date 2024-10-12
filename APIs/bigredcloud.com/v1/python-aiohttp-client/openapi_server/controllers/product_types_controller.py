from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_owner_type_dto import PageResultOwnerTypeDto
from openapi_server import util


async def product_types_get(request: web.Request, ) -> web.Response:
    """Returns a list of global Product Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)
