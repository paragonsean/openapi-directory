from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_firewall_inbound_firewall_rules_request import UpdateNetworkApplianceFirewallInboundFirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l3_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest
from openapi_server import util


async def get_network_appliance_firewall_l3_firewall_rules_2(request: web.Request, network_id) -> web.Response:
    """Return the L3 firewall rules for an MX network

    Return the L3 firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_firewall_l3_firewall_rules_3(request: web.Request, network_id, number) -> web.Response:
    """Return the L3 firewall rules for an SSID on an MR network

    Return the L3 firewall rules for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_appliance_firewall_l3_firewall_rules_2(request: web.Request, network_id, body=None) -> web.Response:
    """Update the L3 firewall rules of an MX network

    Update the L3 firewall rules of an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_firewall_l3_firewall_rules_3(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the L3 firewall rules of an SSID on an MR network

    Update the L3 firewall rules of an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)
