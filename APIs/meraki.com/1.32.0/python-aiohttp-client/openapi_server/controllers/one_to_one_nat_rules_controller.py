from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_firewall_one_to_one_nat_rules_request import UpdateNetworkApplianceFirewallOneToOneNatRulesRequest
from openapi_server import util


async def get_network_appliance_firewall_one_to_one_nat_rules_2(request: web.Request, network_id) -> web.Response:
    """Return the 1:1 NAT mapping rules for an MX network

    Return the 1:1 NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_firewall_one_to_one_nat_rules_2(request: web.Request, network_id, body) -> web.Response:
    """Set the 1:1 NAT mapping rules for an MX network

    Set the 1:1 NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceFirewallOneToOneNatRulesRequest.from_dict(body)
    return web.Response(status=200)
