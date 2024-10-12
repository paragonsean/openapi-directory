from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_switch_dhcp_server_policy_arp_inspection_trusted_server_request import CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest
from openapi_server.models.get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers200_response_inner import GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner
from openapi_server.models.get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device200_response_inner import GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner
from openapi_server.models.update_network_switch_dhcp_server_policy_arp_inspection_trusted_server_request import UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest
from openapi_server import util


async def create_network_switch_dhcp_server_policy_arp_inspection_trusted_server_2(request: web.Request, network_id, body) -> web.Response:
    """Add a server to be trusted by Dynamic ARP Inspection on this network

    Add a server to be trusted by Dynamic ARP Inspection on this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_switch_dhcp_server_policy_arp_inspection_trusted_server_2(request: web.Request, network_id, trusted_server_id) -> web.Response:
    """Remove a server from being trusted by Dynamic ARP Inspection on this network

    Remove a server from being trusted by Dynamic ARP Inspection on this network

    :param network_id: 
    :type network_id: str
    :param trusted_server_id: 
    :type trusted_server_id: str

    """
    return web.Response(status=200)


async def get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers_2(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the list of servers trusted by Dynamic ARP Inspection on this network

    Return the list of servers trusted by Dynamic ARP Inspection on this network. These are also known as whitelisted snoop entries

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device_2(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the devices that have a Dynamic ARP Inspection warning and their warnings

    Return the devices that have a Dynamic ARP Inspection warning and their warnings

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def update_network_switch_dhcp_server_policy_arp_inspection_trusted_server_2(request: web.Request, network_id, trusted_server_id, body=None) -> web.Response:
    """Update a server that is trusted by Dynamic ARP Inspection on this network

    Update a server that is trusted by Dynamic ARP Inspection on this network

    :param network_id: 
    :type network_id: str
    :param trusted_server_id: 
    :type trusted_server_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.from_dict(body)
    return web.Response(status=200)
