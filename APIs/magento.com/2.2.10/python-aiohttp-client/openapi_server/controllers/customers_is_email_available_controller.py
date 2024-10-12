from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_account_management_v1_is_email_available_post_request import CustomerAccountManagementV1IsEmailAvailablePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_is_email_available_post(request: web.Request, body=None) -> web.Response:
    """customers/isEmailAvailable

    Check if given email is associated with a customer account in given website.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerAccountManagementV1IsEmailAvailablePostRequest.from_dict(body)
    return web.Response(status=200)
