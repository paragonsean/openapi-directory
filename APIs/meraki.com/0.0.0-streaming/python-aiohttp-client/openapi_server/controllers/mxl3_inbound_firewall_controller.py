from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_firewall_inbound_firewall_rules_request import UpdateNetworkApplianceFirewallInboundFirewallRulesRequest
from openapi_server import util


async def get_network_appliance_firewall_inbound_firewall_rules(request: web.Request, network_id) -> web.Response:
    """Return the inbound firewall rules for an MX network

    Return the inbound firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_firewall_inbound_firewall_rules(request: web.Request, network_id, body=None) -> web.Response:
    """Update the inbound firewall rules of an MX network

    Update the inbound firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)
