from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_account_management_v1_activate_by_id_put_request import CustomerAccountManagementV1ActivateByIdPutRequest
from openapi_server.models.customer_data_customer_interface import CustomerDataCustomerInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_activate_put(request: web.Request, email, body=None) -> web.Response:
    """customers/{email}/activate

    Activate a customer account using a key that was sent in a confirmation email.

    :param email: 
    :type email: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomerAccountManagementV1ActivateByIdPutRequest.from_dict(body)
    return web.Response(status=200)
