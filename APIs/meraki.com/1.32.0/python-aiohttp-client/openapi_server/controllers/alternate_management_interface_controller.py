from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_switch_alternate_management_interface_request import UpdateNetworkSwitchAlternateManagementInterfaceRequest
from openapi_server.models.update_network_wireless_alternate_management_interface_request import UpdateNetworkWirelessAlternateManagementInterfaceRequest
from openapi_server import util


async def get_network_switch_alternate_management_interface_1(request: web.Request, network_id) -> web.Response:
    """Return the switch alternate management interface for the network

    Return the switch alternate management interface for the network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_alternate_management_interface_1(request: web.Request, network_id) -> web.Response:
    """Return alternate management interface and devices with IP assigned

    Return alternate management interface and devices with IP assigned

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_alternate_management_interface_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the switch alternate management interface for the network

    Update the switch alternate management interface for the network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchAlternateManagementInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_alternate_management_interface_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update alternate management interface and device static IP

    Update alternate management interface and device static IP

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessAlternateManagementInterfaceRequest.from_dict(body)
    return web.Response(status=200)
