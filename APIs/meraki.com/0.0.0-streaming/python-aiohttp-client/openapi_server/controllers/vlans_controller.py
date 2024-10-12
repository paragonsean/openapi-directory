from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_vlan_request import CreateNetworkVlanRequest
from openapi_server.models.update_network_vlan_request import UpdateNetworkVlanRequest
from openapi_server.models.update_network_vlans_enabled_state_request import UpdateNetworkVlansEnabledStateRequest
from openapi_server import util


async def create_network_vlan(request: web.Request, network_id, body) -> web.Response:
    """Add a VLAN

    Add a VLAN

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkVlanRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_vlan(request: web.Request, network_id, vlan_id) -> web.Response:
    """Delete a VLAN from a network

    Delete a VLAN from a network

    :param network_id: 
    :type network_id: str
    :param vlan_id: 
    :type vlan_id: str

    """
    return web.Response(status=200)


async def get_network_vlan(request: web.Request, network_id, vlan_id) -> web.Response:
    """Return a VLAN

    Return a VLAN

    :param network_id: 
    :type network_id: str
    :param vlan_id: 
    :type vlan_id: str

    """
    return web.Response(status=200)


async def get_network_vlans(request: web.Request, network_id) -> web.Response:
    """List the VLANs for an MX network

    List the VLANs for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_vlans_enabled_state(request: web.Request, network_id) -> web.Response:
    """Returns the enabled status of VLANs for the network

    Returns the enabled status of VLANs for the network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_vlan(request: web.Request, network_id, vlan_id, body=None) -> web.Response:
    """Update a VLAN

    Update a VLAN

    :param network_id: 
    :type network_id: str
    :param vlan_id: 
    :type vlan_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkVlanRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_vlans_enabled_state(request: web.Request, network_id, body) -> web.Response:
    """Enable/Disable VLANs for the given network

    Enable/Disable VLANs for the given network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkVlansEnabledStateRequest.from_dict(body)
    return web.Response(status=200)
