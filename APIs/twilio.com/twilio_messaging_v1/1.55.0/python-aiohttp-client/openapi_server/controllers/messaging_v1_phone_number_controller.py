from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_phone_number_response import ListPhoneNumberResponse
from openapi_server.models.messaging_v1_service_phone_number import MessagingV1ServicePhoneNumber
from openapi_server import util


async def create_phone_number(request: web.Request, service_sid, phone_number_sid) -> web.Response:
    """create_phone_number

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the resource under.
    :type service_sid: str
    :param phone_number_sid: The SID of the Phone Number being added to the Service.
    :type phone_number_sid: str

    """
    return web.Response(status=200)


async def delete_phone_number(request: web.Request, service_sid, sid) -> web.Response:
    """delete_phone_number

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.
    :type service_sid: str
    :param sid: The SID of the PhoneNumber resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_phone_number(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_phone_number

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the resource from.
    :type service_sid: str
    :param sid: The SID of the PhoneNumber resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_phone_number(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_phone_number

    

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the resources from.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
