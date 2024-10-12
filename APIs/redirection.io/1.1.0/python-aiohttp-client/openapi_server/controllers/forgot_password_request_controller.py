from typing import List, Dict
from aiohttp import web

from openapi_server.models.forgot_password_request import ForgotPasswordRequest
from openapi_server import util


async def post_forgot_password_request_collection(request: web.Request, forgot_password_request=None) -> web.Response:
    """Creates a ForgotPasswordRequest resource.

    

    :param forgot_password_request: The new ForgotPasswordRequest resource
    :type forgot_password_request: dict | bytes

    """
    forgot_password_request = ForgotPasswordRequest.from_dict(forgot_password_request)
    return web.Response(status=200)
