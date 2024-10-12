from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_cellular_gateway_settings_request import UpdateDeviceCellularGatewaySettingsRequest
from openapi_server import util


async def get_device_cellular_gateway_settings(request: web.Request, serial) -> web.Response:
    """Show the LAN Settings of a MG

    Show the LAN Settings of a MG

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_device_cellular_gateway_settings(request: web.Request, serial, body=None) -> web.Response:
    """Update the LAN Settings for a single MG.

    Update the LAN Settings for a single MG.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCellularGatewaySettingsRequest.from_dict(body)
    return web.Response(status=200)
