from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_cellular_gateway_settings_port_forwarding_rules_request import UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest
from openapi_server import util


async def get_device_cellular_gateway_settings_port_forwarding_rules(request: web.Request, serial) -> web.Response:
    """Returns the port forwarding rules for a single MG.

    Returns the port forwarding rules for a single MG.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_device_cellular_gateway_settings_port_forwarding_rules(request: web.Request, serial, body=None) -> web.Response:
    """Updates the port forwarding rules for a single MG.

    Updates the port forwarding rules for a single MG.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCellularGatewaySettingsPortForwardingRulesRequest.from_dict(body)
    return web.Response(status=200)
