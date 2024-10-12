from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_cellular_gateway_port_forwarding_rules_request import UpdateDeviceCellularGatewayPortForwardingRulesRequest
from openapi_server.models.update_network_appliance_firewall_port_forwarding_rules_request import UpdateNetworkApplianceFirewallPortForwardingRulesRequest
from openapi_server import util


async def get_device_cellular_gateway_port_forwarding_rules_1(request: web.Request, serial) -> web.Response:
    """Returns the port forwarding rules for a single MG.

    Returns the port forwarding rules for a single MG.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_port_forwarding_rules_2(request: web.Request, network_id) -> web.Response:
    """Return the port forwarding rules for an MX network

    Return the port forwarding rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_device_cellular_gateway_port_forwarding_rules_1(request: web.Request, serial, body=None) -> web.Response:
    """Updates the port forwarding rules for a single MG.

    Updates the port forwarding rules for a single MG.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCellularGatewayPortForwardingRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_firewall_port_forwarding_rules_2(request: web.Request, network_id, body) -> web.Response:
    """Update the port forwarding rules for an MX network

    Update the port forwarding rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallPortForwardingRulesRequest.from_dict(body)
    return web.Response(status=200)
