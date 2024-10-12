from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_ssid_l3_firewall_rules_request import UpdateNetworkSsidL3FirewallRulesRequest
from openapi_server import util


async def get_network_ssid_l3_firewall_rules(request: web.Request, network_id, number) -> web.Response:
    """Return the L3 firewall rules for an SSID on an MR network

    Return the L3 firewall rules for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_ssid_l3_firewall_rules(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the L3 firewall rules of an SSID on an MR network

    Update the L3 firewall rules of an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSsidL3FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)
