from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_cellular_gateway_dhcp200_response import GetNetworkCellularGatewayDhcp200Response
from openapi_server.models.get_network_switch_dhcp_v4_servers_seen200_response_inner import GetNetworkSwitchDhcpV4ServersSeen200ResponseInner
from openapi_server.models.update_device_switch_routing_interface_dhcp_request import UpdateDeviceSwitchRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_cellular_gateway_dhcp_request import UpdateNetworkCellularGatewayDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_dhcp_request import UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest
from openapi_server import util


async def get_device_appliance_dhcp_subnets_1(request: web.Request, serial) -> web.Response:
    """Return the DHCP subnet information for an appliance

    Return the DHCP subnet information for an appliance

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_interface_dhcp_3(request: web.Request, serial, interface_id) -> web.Response:
    """Return a layer 3 interface DHCP configuration for a switch

    Return a layer 3 interface DHCP configuration for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_network_cellular_gateway_dhcp_1(request: web.Request, network_id) -> web.Response:
    """List common DHCP settings of MGs

    List common DHCP settings of MGs

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_dhcp_v4_servers_seen_1(request: web.Request, network_id, t0=None, timespan=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

    Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_interface_dhcp_4(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
    """Return a layer 3 interface DHCP configuration for a switch stack

    Return a layer 3 interface DHCP configuration for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def update_device_switch_routing_interface_dhcp_3(request: web.Request, serial, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface DHCP configuration for a switch

    Update a layer 3 interface DHCP configuration for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchRoutingInterfaceDhcpRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_cellular_gateway_dhcp_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update common DHCP settings of MGs

    Update common DHCP settings of MGs

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCellularGatewayDhcpRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_interface_dhcp_4(request: web.Request, network_id, switch_stack_id, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface DHCP configuration for a switch stack

    Update a layer 3 interface DHCP configuration for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.from_dict(body)
    return web.Response(status=200)
