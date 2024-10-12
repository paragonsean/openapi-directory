from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_sip_sip_domain_sip_auth_sip_auth_calls_sip_auth_calls_ip_access_control_list_mapping import ApiV2010AccountSipSipDomainSipAuthSipAuthCallsSipAuthCallsIpAccessControlListMapping
from openapi_server.models.list_sip_auth_calls_ip_access_control_list_mapping_response import ListSipAuthCallsIpAccessControlListMappingResponse
from openapi_server import util


async def create_sip_auth_calls_ip_access_control_list_mapping(request: web.Request, account_sid, domain_sid, ip_access_control_list_sid) -> web.Response:
    """create_sip_auth_calls_ip_access_control_list_mapping

    Create a new IP Access Control List mapping

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param domain_sid: The SID of the SIP domain that will contain the new resource.
    :type domain_sid: str
    :param ip_access_control_list_sid: The SID of the IpAccessControlList resource to map to the SIP domain.
    :type ip_access_control_list_sid: str

    """
    return web.Response(status=200)


async def delete_sip_auth_calls_ip_access_control_list_mapping(request: web.Request, account_sid, domain_sid, sid) -> web.Response:
    """delete_sip_auth_calls_ip_access_control_list_mapping

    Delete an IP Access Control List mapping from the requested domain

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to delete.
    :type account_sid: str
    :param domain_sid: The SID of the SIP domain that contains the resources to delete.
    :type domain_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sip_auth_calls_ip_access_control_list_mapping(request: web.Request, account_sid, domain_sid, sid) -> web.Response:
    """fetch_sip_auth_calls_ip_access_control_list_mapping

    Fetch a specific instance of an IP Access Control List mapping

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resource to fetch.
    :type account_sid: str
    :param domain_sid: The SID of the SIP domain that contains the resource to fetch.
    :type domain_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the IpAccessControlListMapping resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sip_auth_calls_ip_access_control_list_mapping(request: web.Request, account_sid, domain_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sip_auth_calls_ip_access_control_list_mapping

    Retrieve a list of IP Access Control List mappings belonging to the domain used in the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IpAccessControlListMapping resources to read.
    :type account_sid: str
    :param domain_sid: The SID of the SIP domain that contains the resources to read.
    :type domain_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
