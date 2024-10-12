from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_group_interface import CustomerDataGroupInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_group_management_v1_get_default_group_get(request: web.Request, store_id=None) -> web.Response:
    """customerGroups/default

    Get default customer group.

    :param store_id: 
    :type store_id: int

    """
    return web.Response(status=200)
