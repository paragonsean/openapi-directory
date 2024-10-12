from typing import List, Dict
from aiohttp import web

from openapi_server.models.email_validation400_response import EmailValidation400Response
from openapi_server.models.phone_validation200_response import PhoneValidation200Response
from openapi_server import util


async def phone_validation(request: web.Request, your_api_key_here, user_phone_here, country=None) -> web.Response:
    """Phone Validation

    Phone Validation

    :param your_api_key_here: (Required) YOUR_API_KEY_HERE
    :type your_api_key_here: str
    :param user_phone_here: (Required) USER_PHONE_HERE
    :type user_phone_here: str
    :param country: country
    :type country: str

    """
    return web.Response(status=200)
