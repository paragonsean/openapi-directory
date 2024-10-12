from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_phone_number_response import ListPhoneNumberResponse
from openapi_server.models.proxy_v1_service_phone_number import ProxyV1ServicePhoneNumber
from openapi_server import util


async def create_phone_number(request: web.Request, service_sid, is_reserved=None, phone_number=None, sid=None) -> web.Response:
    """create_phone_number

    Add a Phone Number to a Service&#39;s Proxy Number Pool.

    :param service_sid: The SID parent [Service](https://www.twilio.com/docs/proxy/api/service) resource of the new PhoneNumber resource.
    :type service_sid: str
    :param is_reserved: Whether the new phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.
    :type is_reserved: bool
    :param phone_number: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
    :type phone_number: str
    :param sid: The SID of a Twilio [IncomingPhoneNumber](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) resource that represents the Twilio Number you would like to assign to your Proxy Service.
    :type sid: str

    """
    return web.Response(status=200)


async def delete_phone_number(request: web.Request, service_sid, sid) -> web.Response:
    """delete_phone_number

    Delete a specific Phone Number from a Service.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to delete.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_phone_number(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_phone_number

    Fetch a specific Phone Number.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to fetch.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_phone_number(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_phone_number

    Retrieve a list of all Phone Numbers in the Proxy Number Pool for a Service. A maximum of 100 records will be returned per page.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resources to read.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_phone_number(request: web.Request, service_sid, sid, is_reserved=None) -> web.Response:
    """update_phone_number

    Update a specific Proxy Number.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to update.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to update.
    :type sid: str
    :param is_reserved: Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.
    :type is_reserved: bool

    """
    return web.Response(status=200)
