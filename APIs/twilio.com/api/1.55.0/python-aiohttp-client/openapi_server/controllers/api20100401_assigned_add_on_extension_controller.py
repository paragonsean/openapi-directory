from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on_incoming_phone_number_assigned_add_on_extension import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOnIncomingPhoneNumberAssignedAddOnExtension
from openapi_server.models.list_incoming_phone_number_assigned_add_on_extension_response import ListIncomingPhoneNumberAssignedAddOnExtensionResponse
from openapi_server import util


async def fetch_incoming_phone_number_assigned_add_on_extension(request: web.Request, account_sid, resource_sid, assigned_add_on_sid, sid) -> web.Response:
    """fetch_incoming_phone_number_assigned_add_on_extension

    Fetch an instance of an Extension for the Assigned Add-on.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
    :type account_sid: str
    :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.
    :type resource_sid: str
    :param assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
    :type assigned_add_on_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_incoming_phone_number_assigned_add_on_extension(request: web.Request, account_sid, resource_sid, assigned_add_on_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_incoming_phone_number_assigned_add_on_extension

    Retrieve a list of Extensions for the Assigned Add-on.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    :type account_sid: str
    :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.
    :type resource_sid: str
    :param assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
    :type assigned_add_on_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
