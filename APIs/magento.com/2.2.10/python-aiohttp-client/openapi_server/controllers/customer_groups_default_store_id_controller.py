from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_group_interface import CustomerDataGroupInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def v1_customer_groups_default_store_id_get(request: web.Request, store_id) -> web.Response:
    """customerGroups/default/{storeId}

    Get default customer group.

    :param store_id: 
    :type store_id: int

    """
    return web.Response(status=200)
