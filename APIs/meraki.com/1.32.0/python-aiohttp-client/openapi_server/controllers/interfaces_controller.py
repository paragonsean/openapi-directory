from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_device_switch_routing_interface_request import CreateDeviceSwitchRoutingInterfaceRequest
from openapi_server.models.create_network_switch_stack_routing_interface_request import CreateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server.models.get_device_switch_routing_interfaces200_response_inner import GetDeviceSwitchRoutingInterfaces200ResponseInner
from openapi_server.models.update_device_switch_routing_interface_dhcp_request import UpdateDeviceSwitchRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_dhcp_request import UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_request import UpdateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server import util


async def create_device_switch_routing_interface_2(request: web.Request, serial, body=None) -> web.Response:
    """Create a layer 3 interface for a switch

    Create a layer 3 interface for a switch

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_stack_routing_interface_3(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
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


async def delete_device_switch_routing_interface_2(request: web.Request, serial, interface_id) -> web.Response:
    """Delete a layer 3 interface from the switch

    Delete a layer 3 interface from the switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_stack_routing_interface_3(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
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


async def get_device_switch_routing_interface_2(request: web.Request, serial, interface_id) -> web.Response:
    """Return a layer 3 interface for a switch

    Return a layer 3 interface for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_interface_dhcp_2(request: web.Request, serial, interface_id) -> web.Response:
    """Return a layer 3 interface DHCP configuration for a switch

    Return a layer 3 interface DHCP configuration for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_interfaces_2(request: web.Request, serial) -> web.Response:
    """List layer 3 interfaces for a switch

    List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_interface_3(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
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


async def get_network_switch_stack_routing_interface_dhcp_3(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
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


async def get_network_switch_stack_routing_interfaces_3(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """List layer 3 interfaces for a switch stack

    List layer 3 interfaces for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def update_device_switch_routing_interface_2(request: web.Request, serial, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface for a switch

    Update a layer 3 interface for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_switch_routing_interface_dhcp_2(request: web.Request, serial, interface_id, body=None) -> web.Response:
    """Update a layer 3 interface DHCP configuration for a switch

    Update a layer 3 interface DHCP configuration for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchRoutingInterfaceDhcpRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_interface_3(request: web.Request, network_id, switch_stack_id, interface_id, body=None) -> web.Response:
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


async def update_network_switch_stack_routing_interface_dhcp_3(request: web.Request, network_id, switch_stack_id, interface_id, body=None) -> web.Response:
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
