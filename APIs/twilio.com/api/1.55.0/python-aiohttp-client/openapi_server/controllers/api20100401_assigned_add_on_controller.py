from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on import ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberAssignedAddOn
from openapi_server.models.list_incoming_phone_number_assigned_add_on_response import ListIncomingPhoneNumberAssignedAddOnResponse
from openapi_server import util


async def create_incoming_phone_number_assigned_add_on(request: web.Request, account_sid, resource_sid, installed_add_on_sid) -> web.Response:
    """create_incoming_phone_number_assigned_add_on

    Assign an Add-on installation to the Number specified.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param resource_sid: The SID of the Phone Number to assign the Add-on.
    :type resource_sid: str
    :param installed_add_on_sid: The SID that identifies the Add-on installation.
    :type installed_add_on_sid: str

    """
    return web.Response(status=200)


async def delete_incoming_phone_number_assigned_add_on(request: web.Request, account_sid, resource_sid, sid) -> web.Response:
    """delete_incoming_phone_number_assigned_add_on

    Remove the assignment of an Add-on installation from the Number specified.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to delete.
    :type account_sid: str
    :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.
    :type resource_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_incoming_phone_number_assigned_add_on(request: web.Request, account_sid, resource_sid, sid) -> web.Response:
    """fetch_incoming_phone_number_assigned_add_on

    Fetch an instance of an Add-on installation currently assigned to this Number.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
    :type account_sid: str
    :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.
    :type resource_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_incoming_phone_number_assigned_add_on(request: web.Request, account_sid, resource_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_incoming_phone_number_assigned_add_on

    Retrieve a list of Add-on installations currently assigned to this Number.

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
    :type account_sid: str
    :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.
    :type resource_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
