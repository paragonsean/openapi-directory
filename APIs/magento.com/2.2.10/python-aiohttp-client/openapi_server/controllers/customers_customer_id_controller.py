from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_customer_repository_v1_save_put_request import CustomerCustomerRepositoryV1SavePutRequest
from openapi_server.models.customer_data_customer_interface import CustomerDataCustomerInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_customer_repository_v1_delete_by_id_delete(request: web.Request, customer_id) -> web.Response:
    """customers/{customerId}

    Delete customer by Customer ID.

    :param customer_id: 
    :type customer_id: int

    """
    return web.Response(status=200)


async def v1_customers_customer_id_get(request: web.Request, customer_id) -> web.Response:
    """customers/{customerId}

    Get customer by Customer ID.

    :param customer_id: 
    :type customer_id: int

    """
    return web.Response(status=200)


async def v1_customers_customer_id_put(request: web.Request, customer_id, body=None) -> web.Response:
    """customers/{customerId}

    Create or update a customer.

    :param customer_id: 
    :type customer_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomerCustomerRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
