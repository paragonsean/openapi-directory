from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def v1_customers_customer_id_carts_post(request: web.Request, customer_id) -> web.Response:
    """customers/{customerId}/carts

    Creates an empty cart and quote for a specified customer if customer does not have a cart yet.

    :param customer_id: The customer ID.
    :type customer_id: int

    """
    return web.Response(status=200)
