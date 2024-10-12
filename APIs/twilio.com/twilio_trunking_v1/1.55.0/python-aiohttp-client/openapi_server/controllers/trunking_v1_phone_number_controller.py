from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_phone_number_response import ListPhoneNumberResponse
from openapi_server.models.trunking_v1_trunk_phone_number import TrunkingV1TrunkPhoneNumber
from openapi_server import util


async def create_phone_number(request: web.Request, trunk_sid, phone_number_sid) -> web.Response:
    """create_phone_number

    

    :param trunk_sid: The SID of the Trunk to associate the phone number with.
    :type trunk_sid: str
    :param phone_number_sid: The SID of the [Incoming Phone Number](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) that you want to associate with the trunk.
    :type phone_number_sid: str

    """
    return web.Response(status=200)


async def delete_phone_number(request: web.Request, trunk_sid, sid) -> web.Response:
    """delete_phone_number

    

    :param trunk_sid: The SID of the Trunk from which to delete the PhoneNumber resource.
    :type trunk_sid: str
    :param sid: The unique string that we created to identify the PhoneNumber resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_phone_number(request: web.Request, trunk_sid, sid) -> web.Response:
    """fetch_phone_number

    

    :param trunk_sid: The SID of the Trunk from which to fetch the PhoneNumber resource.
    :type trunk_sid: str
    :param sid: The unique string that we created to identify the PhoneNumber resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_phone_number(request: web.Request, trunk_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_phone_number

    

    :param trunk_sid: The SID of the Trunk from which to read the PhoneNumber resources.
    :type trunk_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
