from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_vpn_bgp_request import UpdateNetworkApplianceVpnBgpRequest
from openapi_server import util


async def get_network_appliance_vpn_bgp_2(request: web.Request, network_id) -> web.Response:
    """Return a Hub BGP Configuration

    Return a Hub BGP Configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_vpn_bgp_2(request: web.Request, network_id, body) -> web.Response:
    """Update a Hub BGP Configuration

    Update a Hub BGP Configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVpnBgpRequest.from_dict(body)
    return web.Response(status=200)
