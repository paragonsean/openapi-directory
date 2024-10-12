from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_switch_settings_qos_rule_request import CreateNetworkSwitchSettingsQosRuleRequest
from openapi_server.models.update_network_switch_settings_multicast_request import UpdateNetworkSwitchSettingsMulticastRequest
from openapi_server.models.update_network_switch_settings_qos_rule_request import UpdateNetworkSwitchSettingsQosRuleRequest
from openapi_server.models.update_network_switch_settings_qos_rules_order_request import UpdateNetworkSwitchSettingsQosRulesOrderRequest
from openapi_server.models.update_network_switch_settings_request import UpdateNetworkSwitchSettingsRequest
from openapi_server.models.update_network_switch_settings_storm_control_request import UpdateNetworkSwitchSettingsStormControlRequest
from openapi_server import util


async def create_network_switch_settings_qos_rule(request: web.Request, network_id, body) -> web.Response:
    """Add a quality of service rule

    Add a quality of service rule

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchSettingsQosRuleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_switch_settings_qos_rule(request: web.Request, network_id, qos_rule_id) -> web.Response:
    """Delete a quality of service rule

    Delete a quality of service rule

    :param network_id: 
    :type network_id: str
    :param qos_rule_id: 
    :type qos_rule_id: str

    """
    return web.Response(status=200)


async def get_network_switch_settings(request: web.Request, network_id) -> web.Response:
    """Returns the switch network settings

    Returns the switch network settings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_settings_mtu(request: web.Request, network_id) -> web.Response:
    """Return the MTU configuration

    Return the MTU configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_settings_multicast(request: web.Request, network_id) -> web.Response:
    """Return multicast settings for a network

    Return multicast settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_settings_qos_rule(request: web.Request, network_id, qos_rule_id) -> web.Response:
    """Return a quality of service rule

    Return a quality of service rule

    :param network_id: 
    :type network_id: str
    :param qos_rule_id: 
    :type qos_rule_id: str

    """
    return web.Response(status=200)


async def get_network_switch_settings_qos_rules(request: web.Request, network_id) -> web.Response:
    """List quality of service rules

    List quality of service rules

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_settings_qos_rules_order(request: web.Request, network_id) -> web.Response:
    """Return the quality of service rule IDs by order in which they will be processed by the switch

    Return the quality of service rule IDs by order in which they will be processed by the switch

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_settings_storm_control(request: web.Request, network_id) -> web.Response:
    """Return the storm control configuration for a switch network

    Return the storm control configuration for a switch network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Update switch network settings

    Update switch network settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_settings_multicast(request: web.Request, network_id, body=None) -> web.Response:
    """Update multicast settings for a network

    Update multicast settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchSettingsMulticastRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_settings_qos_rule(request: web.Request, network_id, qos_rule_id, body=None) -> web.Response:
    """Update a quality of service rule

    Update a quality of service rule

    :param network_id: 
    :type network_id: str
    :param qos_rule_id: 
    :type qos_rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchSettingsQosRuleRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_settings_qos_rules_order(request: web.Request, network_id, body) -> web.Response:
    """Update the order in which the rules should be processed by the switch

    Update the order in which the rules should be processed by the switch

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchSettingsQosRulesOrderRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_settings_storm_control(request: web.Request, network_id, body=None) -> web.Response:
    """Update the storm control configuration for a switch network

    Update the storm control configuration for a switch network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchSettingsStormControlRequest.from_dict(body)
    return web.Response(status=200)
