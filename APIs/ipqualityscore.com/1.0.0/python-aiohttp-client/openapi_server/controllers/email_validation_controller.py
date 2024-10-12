from typing import List, Dict
from aiohttp import web

from openapi_server.models.email_validation200_response import EmailValidation200Response
from openapi_server.models.email_validation400_response import EmailValidation400Response
from openapi_server import util


async def email_validation(request: web.Request, your_api_key_here, user_email_here) -> web.Response:
    """Email Validation

    Email Validation

    :param your_api_key_here: (Required) YOUR_API_KEY_HERE
    :type your_api_key_here: str
    :param user_email_here: (Required) USER_EMAIL_HERE
    :type user_email_here: str

    """
    return web.Response(status=200)
