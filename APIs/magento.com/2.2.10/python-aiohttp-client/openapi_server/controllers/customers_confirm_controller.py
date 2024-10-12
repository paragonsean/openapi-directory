from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_account_management_v1_resend_confirmation_post_request import CustomerAccountManagementV1ResendConfirmationPostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_resend_confirmation_post(request: web.Request, body=None) -> web.Response:
    """customers/confirm

    Resend confirmation email.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerAccountManagementV1ResendConfirmationPostRequest.from_dict(body)
    return web.Response(status=200)
