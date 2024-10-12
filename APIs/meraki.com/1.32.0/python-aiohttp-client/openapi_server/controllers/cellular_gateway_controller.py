from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_cellular_gateway_dhcp200_response import GetNetworkCellularGatewayDhcp200Response
from openapi_server.models.get_organization_cellular_gateway_uplink_statuses200_response_inner import GetOrganizationCellularGatewayUplinkStatuses200ResponseInner
from openapi_server.models.update_device_cellular_gateway_lan_request import UpdateDeviceCellularGatewayLanRequest
from openapi_server.models.update_device_cellular_gateway_port_forwarding_rules_request import UpdateDeviceCellularGatewayPortForwardingRulesRequest
from openapi_server.models.update_network_cellular_gateway_connectivity_monitoring_destinations_request import UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest
from openapi_server.models.update_network_cellular_gateway_dhcp_request import UpdateNetworkCellularGatewayDhcpRequest
from openapi_server.models.update_network_cellular_gateway_subnet_pool_request import UpdateNetworkCellularGatewaySubnetPoolRequest
from openapi_server.models.update_network_cellular_gateway_uplink_request import UpdateNetworkCellularGatewayUplinkRequest
from openapi_server import util


async def get_device_cellular_gateway_lan(request: web.Request, serial) -> web.Response:
    """Show the LAN Settings of a MG

    Show the LAN Settings of a MG

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_cellular_gateway_port_forwarding_rules(request: web.Request, serial) -> web.Response:
    """Returns the port forwarding rules for a single MG.

    Returns the port forwarding rules for a single MG.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_cellular_gateway_connectivity_monitoring_destinations(request: web.Request, network_id) -> web.Response:
    """Return the connectivity testing destinations for an MG network

    Return the connectivity testing destinations for an MG network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_cellular_gateway_dhcp(request: web.Request, network_id) -> web.Response:
    """List common DHCP settings of MGs

    List common DHCP settings of MGs

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_cellular_gateway_subnet_pool(request: web.Request, network_id) -> web.Response:
    """Return the subnet pool and mask configured for MGs in the network.

    Return the subnet pool and mask configured for MGs in the network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_cellular_gateway_uplink(request: web.Request, network_id) -> web.Response:
    """Returns the uplink settings for your MG network.

    Returns the uplink settings for your MG network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_cellular_gateway_uplink_statuses(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MG cellular gateway in the organization

    List the uplink status of every Meraki MG cellular gateway in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of network IDs. The returned devices will be filtered to only include these networks.
    :type network_ids: List[str]
    :param serials: A list of serial numbers. The returned devices will be filtered to only include these serials.
    :type serials: List[str]
    :param iccids: A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    :type iccids: List[str]

    """
    return web.Response(status=200)


async def update_device_cellular_gateway_lan(request: web.Request, serial, body=None) -> web.Response:
    """Update the LAN Settings for a single MG.

    Update the LAN Settings for a single MG.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCellularGatewayLanRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_cellular_gateway_port_forwarding_rules(request: web.Request, serial, body=None) -> web.Response:
    """Updates the port forwarding rules for a single MG.

    Updates the port forwarding rules for a single MG.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCellularGatewayPortForwardingRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_cellular_gateway_connectivity_monitoring_destinations(request: web.Request, network_id, body=None) -> web.Response:
    """Update the connectivity testing destinations for an MG network

    Update the connectivity testing destinations for an MG network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_cellular_gateway_dhcp(request: web.Request, network_id, body=None) -> web.Response:
    """Update common DHCP settings of MGs

    Update common DHCP settings of MGs

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCellularGatewayDhcpRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_cellular_gateway_subnet_pool(request: web.Request, network_id, body=None) -> web.Response:
    """Update the subnet pool and mask configuration for MGs in the network.

    Update the subnet pool and mask configuration for MGs in the network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCellularGatewaySubnetPoolRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_cellular_gateway_uplink(request: web.Request, network_id, body=None) -> web.Response:
    """Updates the uplink settings for your MG network.

    Updates the uplink settings for your MG network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCellularGatewayUplinkRequest.from_dict(body)
    return web.Response(status=200)
