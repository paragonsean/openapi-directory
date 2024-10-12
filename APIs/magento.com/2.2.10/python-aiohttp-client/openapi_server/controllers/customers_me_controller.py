from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_customer_repository_v1_save_put_request import CustomerCustomerRepositoryV1SavePutRequest
from openapi_server.models.customer_data_customer_interface import CustomerDataCustomerInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_customer_repository_v1_get_by_id_get(request: web.Request, ) -> web.Response:
    """customers/me

    Get customer by Customer ID.


    """
    return web.Response(status=200)


async def customer_customer_repository_v1_save_put(request: web.Request, body=None) -> web.Response:
    """customers/me

    Create or update a customer.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerCustomerRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
