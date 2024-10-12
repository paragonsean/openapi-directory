from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_ip_access_control_list_response import ListIpAccessControlListResponse
from openapi_server.models.trunking_v1_trunk_ip_access_control_list import TrunkingV1TrunkIpAccessControlList
from openapi_server import util


async def create_ip_access_control_list(request: web.Request, trunk_sid, ip_access_control_list_sid) -> web.Response:
    """create_ip_access_control_list

    Associate an IP Access Control List with a Trunk

    :param trunk_sid: The SID of the Trunk to associate the IP Access Control List with.
    :type trunk_sid: str
    :param ip_access_control_list_sid: The SID of the [IP Access Control List](https://www.twilio.com/docs/voice/sip/api/sip-ipaccesscontrollist-resource) that you want to associate with the trunk.
    :type ip_access_control_list_sid: str

    """
    return web.Response(status=200)


async def delete_ip_access_control_list(request: web.Request, trunk_sid, sid) -> web.Response:
    """delete_ip_access_control_list

    Remove an associated IP Access Control List from a Trunk

    :param trunk_sid: The SID of the Trunk from which to delete the IP Access Control List.
    :type trunk_sid: str
    :param sid: The unique string that we created to identify the IpAccessControlList resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_ip_access_control_list(request: web.Request, trunk_sid, sid) -> web.Response:
    """fetch_ip_access_control_list

    

    :param trunk_sid: The SID of the Trunk from which to fetch the IP Access Control List.
    :type trunk_sid: str
    :param sid: The unique string that we created to identify the IpAccessControlList resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_ip_access_control_list(request: web.Request, trunk_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_ip_access_control_list

    List all IP Access Control Lists for a Trunk

    :param trunk_sid: The SID of the Trunk from which to read the IP Access Control Lists.
    :type trunk_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
