from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_cellular_gateway_lan_request import UpdateDeviceCellularGatewayLanRequest
from openapi_server import util


async def get_device_cellular_gateway_lan_1(request: web.Request, serial) -> web.Response:
    """Show the LAN Settings of a MG

    Show the LAN Settings of a MG

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_device_cellular_gateway_lan_1(request: web.Request, serial, body=None) -> web.Response:
    """Update the LAN Settings for a single MG.

    Update the LAN Settings for a single MG.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCellularGatewayLanRequest.from_dict(body)
    return web.Response(status=200)
