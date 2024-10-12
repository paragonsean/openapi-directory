from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_switch_qos_rule_request import CreateNetworkSwitchQosRuleRequest
from openapi_server.models.update_network_switch_qos_rule_request import UpdateNetworkSwitchQosRuleRequest
from openapi_server.models.update_network_switch_qos_rules_order_request import UpdateNetworkSwitchQosRulesOrderRequest
from openapi_server import util


async def create_network_switch_qos_rule_1(request: web.Request, network_id, body) -> web.Response:
    """Add a quality of service rule

    Add a quality of service rule

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchQosRuleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_switch_qos_rule_1(request: web.Request, network_id, qos_rule_id) -> web.Response:
    """Delete a quality of service rule

    Delete a quality of service rule

    :param network_id: 
    :type network_id: str
    :param qos_rule_id: 
    :type qos_rule_id: str

    """
    return web.Response(status=200)


async def get_network_switch_qos_rule_1(request: web.Request, network_id, qos_rule_id) -> web.Response:
    """Return a quality of service rule

    Return a quality of service rule

    :param network_id: 
    :type network_id: str
    :param qos_rule_id: 
    :type qos_rule_id: str

    """
    return web.Response(status=200)


async def get_network_switch_qos_rules_1(request: web.Request, network_id) -> web.Response:
    """List quality of service rules

    List quality of service rules

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_qos_rules_order_1(request: web.Request, network_id) -> web.Response:
    """Return the quality of service rule IDs by order in which they will be processed by the switch

    Return the quality of service rule IDs by order in which they will be processed by the switch

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_qos_rule_1(request: web.Request, network_id, qos_rule_id, body=None) -> web.Response:
    """Update a quality of service rule

    Update a quality of service rule

    :param network_id: 
    :type network_id: str
    :param qos_rule_id: 
    :type qos_rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchQosRuleRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_qos_rules_order_1(request: web.Request, network_id, body) -> web.Response:
    """Update the order in which the rules should be processed by the switch

    Update the order in which the rules should be processed by the switch

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchQosRulesOrderRequest.from_dict(body)
    return web.Response(status=200)
