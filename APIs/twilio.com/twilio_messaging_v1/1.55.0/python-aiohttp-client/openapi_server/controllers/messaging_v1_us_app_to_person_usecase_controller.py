from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_service_us_app_to_person_usecase import MessagingV1ServiceUsAppToPersonUsecase
from openapi_server import util


async def fetch_us_app_to_person_usecase(request: web.Request, messaging_service_sid, brand_registration_sid=None) -> web.Response:
    """fetch_us_app_to_person_usecase

    

    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.
    :type messaging_service_sid: str
    :param brand_registration_sid: The unique string to identify the A2P brand.
    :type brand_registration_sid: str

    """
    return web.Response(status=200)
