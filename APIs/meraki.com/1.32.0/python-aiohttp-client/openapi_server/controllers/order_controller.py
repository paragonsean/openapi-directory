from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_switch_qos_rules_order_request import UpdateNetworkSwitchQosRulesOrderRequest
from openapi_server import util


async def get_network_switch_qos_rules_order_2(request: web.Request, network_id) -> web.Response:
    """Return the quality of service rule IDs by order in which they will be processed by the switch

    Return the quality of service rule IDs by order in which they will be processed by the switch

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_qos_rules_order_2(request: web.Request, network_id, body) -> web.Response:
    """Update the order in which the rules should be processed by the switch

    Update the order in which the rules should be processed by the switch

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchQosRulesOrderRequest.from_dict(body)
    return web.Response(status=200)
