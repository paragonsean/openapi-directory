from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_port_request import UpdateNetworkAppliancePortRequest
from openapi_server import util


async def get_network_appliance_port(request: web.Request, network_id, appliance_port_id) -> web.Response:
    """Return per-port VLAN settings for a single MX port.

    Return per-port VLAN settings for a single MX port.

    :param network_id: 
    :type network_id: str
    :param appliance_port_id: 
    :type appliance_port_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_ports(request: web.Request, network_id) -> web.Response:
    """List per-port VLAN settings for all ports of a MX.

    List per-port VLAN settings for all ports of a MX.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_port(request: web.Request, network_id, appliance_port_id, body=None) -> web.Response:
    """Update the per-port VLAN settings for a single MX port.

    Update the per-port VLAN settings for a single MX port.

    :param network_id: 
    :type network_id: str
    :param appliance_port_id: 
    :type appliance_port_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkAppliancePortRequest.from_dict(body)
    return web.Response(status=200)
