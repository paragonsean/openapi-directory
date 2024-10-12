from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_sip_sip_ip_access_control_list import ApiV2010AccountSipSipIpAccessControlList
from openapi_server.models.list_sip_ip_access_control_list_response import ListSipIpAccessControlListResponse
from openapi_server import util


async def create_sip_ip_access_control_list(request: web.Request, account_sid, friendly_name) -> web.Response:
    """create_sip_ip_access_control_list

    Create a new IpAccessControlList resource

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param friendly_name: A human readable descriptive text that describes the IpAccessControlList, up to 255 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_sip_ip_access_control_list(request: web.Request, account_sid, sid) -> web.Response:
    """delete_sip_ip_access_control_list

    Delete an IpAccessControlList from the requested account

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param sid: A 34 character string that uniquely identifies the resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sip_ip_access_control_list(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_sip_ip_access_control_list

    Fetch a specific instance of an IpAccessControlList

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param sid: A 34 character string that uniquely identifies the resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sip_ip_access_control_list(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sip_ip_access_control_list

    Retrieve a list of IpAccessControlLists that belong to the account used to make the request

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sip_ip_access_control_list(request: web.Request, account_sid, sid, friendly_name) -> web.Response:
    """update_sip_ip_access_control_list

    Rename an IpAccessControlList

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param sid: A 34 character string that uniquely identifies the resource to udpate.
    :type sid: str
    :param friendly_name: A human readable descriptive text, up to 255 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
