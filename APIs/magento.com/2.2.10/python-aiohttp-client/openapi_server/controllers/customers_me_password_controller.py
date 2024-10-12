from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_account_management_v1_change_password_by_id_put_request import CustomerAccountManagementV1ChangePasswordByIdPutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_change_password_by_id_put(request: web.Request, body=None) -> web.Response:
    """customers/me/password

    Change customer password.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerAccountManagementV1ChangePasswordByIdPutRequest.from_dict(body)
    return web.Response(status=200)
