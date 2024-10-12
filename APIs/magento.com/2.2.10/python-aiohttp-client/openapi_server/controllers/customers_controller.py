from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_account_management_v1_create_account_post_request import CustomerAccountManagementV1CreateAccountPostRequest
from openapi_server.models.customer_data_customer_interface import CustomerDataCustomerInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_create_account_post(request: web.Request, body=None) -> web.Response:
    """customers

    Create customer account. Perform necessary business operations like sending email.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerAccountManagementV1CreateAccountPostRequest.from_dict(body)
    return web.Response(status=200)
