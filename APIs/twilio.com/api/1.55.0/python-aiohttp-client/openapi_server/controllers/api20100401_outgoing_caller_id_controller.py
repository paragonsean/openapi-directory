from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_outgoing_caller_id import ApiV2010AccountOutgoingCallerId
from openapi_server.models.list_outgoing_caller_id_response import ListOutgoingCallerIdResponse
from openapi_server import util


async def delete_outgoing_caller_id(request: web.Request, account_sid, sid) -> web.Response:
    """delete_outgoing_caller_id

    Delete the caller-id specified from the account

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to delete.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_outgoing_caller_id(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_outgoing_caller_id

    Fetch an outgoing-caller-id belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_outgoing_caller_id(request: web.Request, account_sid, phone_number=None, friendly_name=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_outgoing_caller_id

    Retrieve a list of outgoing-caller-ids belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to read.
    :type account_sid: str
    :param phone_number: The phone number of the OutgoingCallerId resources to read.
    :type phone_number: str
    :param friendly_name: The string that identifies the OutgoingCallerId resources to read.
    :type friendly_name: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_outgoing_caller_id(request: web.Request, account_sid, sid, friendly_name=None) -> web.Response:
    """update_outgoing_caller_id

    Updates the caller-id

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
