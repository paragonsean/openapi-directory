from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_get_confirmation_status_get(request: web.Request, customer_id) -> web.Response:
    """customers/{customerId}/confirm

    Gets the account confirmation status.

    :param customer_id: 
    :type customer_id: int

    """
    return web.Response(status=200)
