from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_account_management_v1_reset_password_post_request import CustomerAccountManagementV1ResetPasswordPostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_reset_password_post(request: web.Request, body=None) -> web.Response:
    """customers/resetPassword

    Reset customer password.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerAccountManagementV1ResetPasswordPostRequest.from_dict(body)
    return web.Response(status=200)
