from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_account_management_v1_initiate_password_reset_put_request import CustomerAccountManagementV1InitiatePasswordResetPutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_initiate_password_reset_put(request: web.Request, body=None) -> web.Response:
    """customers/password

    Send an email to the customer with a password reset link.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerAccountManagementV1InitiatePasswordResetPutRequest.from_dict(body)
    return web.Response(status=200)
