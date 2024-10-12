from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_appliance_vlan201_response import CreateNetworkApplianceVlan201Response
from openapi_server.models.create_network_appliance_vlan_request import CreateNetworkApplianceVlanRequest
from openapi_server.models.get_network_appliance_vlans200_response_inner import GetNetworkApplianceVlans200ResponseInner
from openapi_server.models.update_network_appliance_vlan_request import UpdateNetworkApplianceVlanRequest
from openapi_server.models.update_network_appliance_vlans_settings_request import UpdateNetworkApplianceVlansSettingsRequest
from openapi_server import util


async def create_network_appliance_vlan_1(request: web.Request, network_id, body) -> web.Response:
    """Add a VLAN

    Add a VLAN

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkApplianceVlanRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_appliance_vlan_1(request: web.Request, network_id, vlan_id) -> web.Response:
    """Delete a VLAN from a network

    Delete a VLAN from a network

    :param network_id: 
    :type network_id: str
    :param vlan_id: 
    :type vlan_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_vlan_1(request: web.Request, network_id, vlan_id) -> web.Response:
    """Return a VLAN

    Return a VLAN

    :param network_id: 
    :type network_id: str
    :param vlan_id: 
    :type vlan_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_vlans_1(request: web.Request, network_id) -> web.Response:
    """List the VLANs for an MX network

    List the VLANs for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_vlans_settings_1(request: web.Request, network_id) -> web.Response:
    """Returns the enabled status of VLANs for the network

    Returns the enabled status of VLANs for the network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_vlan_1(request: web.Request, network_id, vlan_id, body=None) -> web.Response:
    """Update a VLAN

    Update a VLAN

    :param network_id: 
    :type network_id: str
    :param vlan_id: 
    :type vlan_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVlanRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_vlans_settings_1(request: web.Request, network_id, body=None) -> web.Response:
    """Enable/Disable VLANs for the given network

    Enable/Disable VLANs for the given network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceVlansSettingsRequest.from_dict(body)
    return web.Response(status=200)
