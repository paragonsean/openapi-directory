from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_short_code_response import ListShortCodeResponse
from openapi_server.models.proxy_v1_service_short_code import ProxyV1ServiceShortCode
from openapi_server import util


async def create_short_code(request: web.Request, service_sid, sid) -> web.Response:
    """create_short_code

    Add a Short Code to the Proxy Number Pool for the Service.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    :type service_sid: str
    :param sid: The SID of a Twilio [ShortCode](https://www.twilio.com/en-us/messaging/channels/sms/short-codes) resource that represents the short code you would like to assign to your Proxy Service.
    :type sid: str

    """
    return web.Response(status=200)


async def delete_short_code(request: web.Request, service_sid, sid) -> web.Response:
    """delete_short_code

    Delete a specific Short Code from a Service.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource to delete the ShortCode resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_short_code(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_short_code

    Fetch a specific Short Code.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to fetch the resource from.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_short_code(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_short_code

    Retrieve a list of all Short Codes in the Proxy Number Pool for the Service. A maximum of 100 records will be returned per page.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_short_code(request: web.Request, service_sid, sid, is_reserved=None) -> web.Response:
    """update_short_code

    Update a specific Short Code.

    :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update.
    :type sid: str
    :param is_reserved: Whether the short code should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.
    :type is_reserved: bool

    """
    return web.Response(status=200)
