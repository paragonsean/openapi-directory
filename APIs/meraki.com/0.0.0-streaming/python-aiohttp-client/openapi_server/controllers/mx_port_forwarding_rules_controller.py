from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_port_forwarding_rules_request import UpdateNetworkPortForwardingRulesRequest
from openapi_server import util


async def get_network_port_forwarding_rules(request: web.Request, network_id) -> web.Response:
    """Return the port forwarding rules for an MX network

    Return the port forwarding rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_port_forwarding_rules(request: web.Request, network_id, body) -> web.Response:
    """Update the port forwarding rules for an MX network

    Update the port forwarding rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkPortForwardingRulesRequest.from_dict(body)
    return web.Response(status=200)
