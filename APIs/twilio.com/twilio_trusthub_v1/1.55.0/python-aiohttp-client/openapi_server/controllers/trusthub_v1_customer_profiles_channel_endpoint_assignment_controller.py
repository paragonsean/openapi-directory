from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_customer_profile_channel_endpoint_assignment_response import ListCustomerProfileChannelEndpointAssignmentResponse
from openapi_server.models.trusthub_v1_customer_profile_customer_profile_channel_endpoint_assignment import TrusthubV1CustomerProfileCustomerProfileChannelEndpointAssignment
from openapi_server import util


async def create_customer_profile_channel_endpoint_assignment(request: web.Request, customer_profile_sid, channel_endpoint_sid, channel_endpoint_type) -> web.Response:
    """create_customer_profile_channel_endpoint_assignment

    Create a new Assigned Item.

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param channel_endpoint_sid: The SID of an channel endpoint
    :type channel_endpoint_sid: str
    :param channel_endpoint_type: The type of channel endpoint. eg: phone-number
    :type channel_endpoint_type: str

    """
    return web.Response(status=200)


async def delete_customer_profile_channel_endpoint_assignment(request: web.Request, customer_profile_sid, sid) -> web.Response:
    """delete_customer_profile_channel_endpoint_assignment

    Remove an Assignment Item Instance.

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param sid: The unique string that we created to identify the resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_customer_profile_channel_endpoint_assignment(request: web.Request, customer_profile_sid, sid) -> web.Response:
    """fetch_customer_profile_channel_endpoint_assignment

    Fetch specific Assigned Item Instance.

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param sid: The unique string that we created to identify the resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_customer_profile_channel_endpoint_assignment(request: web.Request, customer_profile_sid, channel_endpoint_sid=None, channel_endpoint_sids=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_customer_profile_channel_endpoint_assignment

    Retrieve a list of all Assigned Items for an account.

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param channel_endpoint_sid: The SID of an channel endpoint
    :type channel_endpoint_sid: str
    :param channel_endpoint_sids: comma separated list of channel endpoint sids
    :type channel_endpoint_sids: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
