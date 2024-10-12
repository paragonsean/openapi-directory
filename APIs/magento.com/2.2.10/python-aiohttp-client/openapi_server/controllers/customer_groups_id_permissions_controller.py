from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_group_management_v1_is_readonly_get(request: web.Request, id) -> web.Response:
    """customerGroups/{id}/permissions

    Check if customer group can be deleted.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
