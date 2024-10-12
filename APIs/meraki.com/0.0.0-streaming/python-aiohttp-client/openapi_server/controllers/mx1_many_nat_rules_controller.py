from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_one_to_many_nat_rules_request import UpdateNetworkOneToManyNatRulesRequest
from openapi_server import util


async def get_network_one_to_many_nat_rules(request: web.Request, network_id) -> web.Response:
    """Return the 1:Many NAT mapping rules for an MX network

    Return the 1:Many NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_one_to_many_nat_rules(request: web.Request, network_id, body) -> web.Response:
    """Set the 1:Many NAT mapping rules for an MX network

    Set the 1:Many NAT mapping rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkOneToManyNatRulesRequest.from_dict(body)
    return web.Response(status=200)
