from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_switch_routing_ospf_request import UpdateNetworkSwitchRoutingOspfRequest
from openapi_server import util


async def get_network_switch_routing_ospf_2(request: web.Request, network_id) -> web.Response:
    """Return layer 3 OSPF routing configuration

    Return layer 3 OSPF routing configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_routing_ospf_2(request: web.Request, network_id, body=None) -> web.Response:
    """Update layer 3 OSPF routing configuration

    Update layer 3 OSPF routing configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchRoutingOspfRequest.from_dict(body)
    return web.Response(status=200)
