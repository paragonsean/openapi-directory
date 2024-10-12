from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_user_defined_field_dto import PageResultUserDefinedFieldDto
from openapi_server import util


async def user_defined_fields_get(request: web.Request, ) -> web.Response:
    """Returns a list of company&#39;s User Defined Fields. Supports OData querying protocol.  Filtering is allowed by \&quot;categoryTypeId\&quot; field.  Ordering is allowed by \&quot;id\&quot; and \&quot;orderIndex\&quot; fields.

    


    """
    return web.Response(status=200)
