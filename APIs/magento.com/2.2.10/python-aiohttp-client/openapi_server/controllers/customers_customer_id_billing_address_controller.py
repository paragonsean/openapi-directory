from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_address_interface import CustomerDataAddressInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def v1_customers_customer_id_billing_address_get(request: web.Request, customer_id) -> web.Response:
    """customers/{customerId}/billingAddress

    Retrieve default billing address for the given customerId.

    :param customer_id: 
    :type customer_id: int

    """
    return web.Response(status=200)
