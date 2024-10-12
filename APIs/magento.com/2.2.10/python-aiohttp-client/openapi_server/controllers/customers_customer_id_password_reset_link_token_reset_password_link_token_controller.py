from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_account_management_v1_validate_reset_password_link_token_get(request: web.Request, customer_id, reset_password_link_token) -> web.Response:
    """customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken}

    Check if password reset token is valid.

    :param customer_id: If 0 is given then a customer will be matched by the RP token.
    :type customer_id: int
    :param reset_password_link_token: 
    :type reset_password_link_token: str

    """
    return web.Response(status=200)
