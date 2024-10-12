from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_brand_registrations_brand_registration_otp import MessagingV1BrandRegistrationsBrandRegistrationOtp
from openapi_server import util


async def create_brand_registration_otp(request: web.Request, brand_registration_sid) -> web.Response:
    """create_brand_registration_otp

    

    :param brand_registration_sid: Brand Registration Sid of Sole Proprietor Brand.
    :type brand_registration_sid: str

    """
    return web.Response(status=200)
