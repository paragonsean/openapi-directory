from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_firewall_l7_firewall_rules_request import UpdateNetworkApplianceFirewallL7FirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l7_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest
from openapi_server import util


async def get_network_appliance_firewall_l7_firewall_rules_2(request: web.Request, network_id) -> web.Response:
    """List the MX L7 firewall rules for an MX network

    List the MX L7 firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_firewall_l7_firewall_rules_application_categories_2(request: web.Request, network_id) -> web.Response:
    """Return the L7 firewall application categories and their associated applications for an MX network

    Return the L7 firewall application categories and their associated applications for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_firewall_l7_firewall_rules_3(request: web.Request, network_id, number) -> web.Response:
    """Return the L7 firewall rules for an SSID on an MR network

    Return the L7 firewall rules for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_appliance_firewall_l7_firewall_rules_2(request: web.Request, network_id, body=None) -> web.Response:
    """Update the MX L7 firewall rules for an MX network

    Update the MX L7 firewall rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallL7FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_firewall_l7_firewall_rules_3(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the L7 firewall rules of an SSID on an MR network

    Update the L7 firewall rules of an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)
