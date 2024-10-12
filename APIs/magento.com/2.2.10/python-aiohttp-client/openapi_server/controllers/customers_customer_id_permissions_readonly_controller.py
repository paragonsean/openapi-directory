from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_is_readonly_get(request: web.Request, customer_id) -> web.Response:
    """customers/{customerId}/permissions/readonly

    Check if customer can be deleted.

    :param customer_id: 
    :type customer_id: int

    """
    return web.Response(status=200)
