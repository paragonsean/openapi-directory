from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_network_switch_stack_request import AddNetworkSwitchStackRequest
from openapi_server.models.create_device_switch_routing_static_route_request import CreateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.create_network_switch_stack_request import CreateNetworkSwitchStackRequest
from openapi_server.models.create_network_switch_stack_routing_interface_request import CreateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server.models.get_network_switch_stack200_response import GetNetworkSwitchStack200Response
from openapi_server.models.remove_network_switch_stack_request import RemoveNetworkSwitchStackRequest
from openapi_server.models.update_device_switch_routing_static_route_request import UpdateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.update_network_switch_stack_routing_interface_dhcp_request import UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_request import UpdateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server import util


async def add_network_switch_stack_1(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
    """Add a switch to a stack

    Add a switch to a stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddNetworkSwitchStackRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_stack_1(request: web.Request, network_id, body) -> web.Response:
    """Create a stack

    Create a stack

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchStackRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_stack_routing_interface_1(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
    """Create a layer 3 interface for a switch stack

    Create a layer 3 interface for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchStackRoutingInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_stack_routing_static_route_1(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
    """Create a layer 3 static route for a switch stack

    Create a layer 3 static route for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_switch_stack_1(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """Delete a stack

    Delete a stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_stack_routing_interface_1(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
    """Delete a layer 3 interface from a switch stack

    Delete a layer 3 interface from a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_stack_routing_static_route_1(request: web.Request, network_id, switch_stack_id, static_route_id) -> web.Response:
    """Delete a layer 3 static route for a switch stack

    Delete a layer 3 static route for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_1(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """Show a switch stack

    Show a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_interface_1(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
    """Return a layer 3 interface from a switch stack

    Return a layer 3 interface from a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_interface_dhcp_1(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
    """Return a layer 3 interface DHCP configuration for a switch stack

    Return a layer 3 interface DHCP configuration for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_interfaces_1(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """List layer 3 interfaces for a switch stack

    List layer 3 interfaces for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_static_route_1(request: web.Request, network_id, switch_stack_id, static_route_id) -> web.Response:
    """Return a layer 3 static route for a switch stack

    Return a layer 3 static route for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_static_routes_1(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """List layer 3 static routes for a switch stack

    List layer 3 static routes for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stacks_1(request: web.Request, network_id) -> web.Response:
    """List the switch stacks in a network

    List the switch stacks in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def remove_network_switch_stack_1(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
    """Remove a switch from a stack

    Remove a switch from a stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveNetworkSwitchStackRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_interface_1(request: web.Request, network_id, switch_stack_id, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface for a switch stack

    Update a layer 3 interface for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchStackRoutingInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_interface_dhcp_1(request: web.Request, network_id, switch_stack_id, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface DHCP configuration for a switch stack

    Update a layer 3 interface DHCP configuration for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_static_route_1(request: web.Request, network_id, switch_stack_id, static_route_id, body=None) -> web.Response:
    """Update a layer 3 static route for a switch stack

    Update a layer 3 static route for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str
    :param static_route_id: 
    :type static_route_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchRoutingStaticRouteRequest.from_dict(body)
    return web.Response(status=200)
