from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_address_interface import CustomerDataAddressInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_get_default_billing_address_get(request: web.Request, ) -> web.Response:
    """customers/me/billingAddress

    Retrieve default billing address for the given customerId.


    """
    return web.Response(status=200)
