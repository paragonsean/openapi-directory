from typing import List, Dict
from aiohttp import web

from openapi_server.models.page_result_owner_type_group_dto import PageResultOwnerTypeGroupDto
from openapi_server import util


async def owner_type_groups_get(request: web.Request, ) -> web.Response:
    """Returns a list of global Owner Type Groups. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

    


    """
    return web.Response(status=200)
