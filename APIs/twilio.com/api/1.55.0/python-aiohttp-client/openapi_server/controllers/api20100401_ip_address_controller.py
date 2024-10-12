from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address import ApiV2010AccountSipSipIpAccessControlListSipIpAddress
from openapi_server.models.list_sip_ip_address_response import ListSipIpAddressResponse
from openapi_server import util


async def create_sip_ip_address(request: web.Request, account_sid, ip_access_control_list_sid, friendly_name, ip_address, cidr_prefix_length=None) -> web.Response:
    """create_sip_ip_address

    Create a new IpAddress resource.

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param ip_access_control_list_sid: The IpAccessControlList Sid with which to associate the created IpAddress resource.
    :type ip_access_control_list_sid: str
    :param friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
    :type friendly_name: str
    :param ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
    :type ip_address: str
    :param cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
    :type cidr_prefix_length: int

    """
    return web.Response(status=200)


async def delete_sip_ip_address(request: web.Request, account_sid, ip_access_control_list_sid, sid) -> web.Response:
    """delete_sip_ip_address

    Delete an IpAddress resource.

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to delete.
    :type ip_access_control_list_sid: str
    :param sid: A 34 character string that uniquely identifies the resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sip_ip_address(request: web.Request, account_sid, ip_access_control_list_sid, sid) -> web.Response:
    """fetch_sip_ip_address

    Read one IpAddress resource.

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to fetch.
    :type ip_access_control_list_sid: str
    :param sid: A 34 character string that uniquely identifies the IpAddress resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sip_ip_address(request: web.Request, account_sid, ip_access_control_list_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sip_ip_address

    Read multiple IpAddress resources.

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to read.
    :type ip_access_control_list_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sip_ip_address(request: web.Request, account_sid, ip_access_control_list_sid, sid, cidr_prefix_length=None, friendly_name=None, ip_address=None) -> web.Response:
    """update_sip_ip_address

    Update an IpAddress resource.

    :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
    :type account_sid: str
    :param ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to update.
    :type ip_access_control_list_sid: str
    :param sid: A 34 character string that identifies the IpAddress resource to update.
    :type sid: str
    :param cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
    :type cidr_prefix_length: int
    :param friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
    :type friendly_name: str
    :param ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
    :type ip_address: str

    """
    return web.Response(status=200)
