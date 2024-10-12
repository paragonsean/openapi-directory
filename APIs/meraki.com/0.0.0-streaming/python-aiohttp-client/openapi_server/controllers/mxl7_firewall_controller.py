from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_l7_firewall_rules_request import UpdateNetworkL7FirewallRulesRequest
from openapi_server import util


async def get_network_l7_firewall_rules(request: web.Request, network_id) -> web.Response:
    """List the MX L7 firewall rules for an MX network

    List the MX L7 firewall rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_l7_firewall_rules(request: web.Request, network_id, body=None) -> web.Response:
    """Update the MX L7 firewall rules for an MX network

    Update the MX L7 firewall rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkL7FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)
