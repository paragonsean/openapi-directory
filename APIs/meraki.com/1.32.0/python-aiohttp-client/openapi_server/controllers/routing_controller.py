from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_device_switch_routing_interface_request import CreateDeviceSwitchRoutingInterfaceRequest
from openapi_server.models.create_device_switch_routing_static_route_request import CreateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.create_network_switch_routing_multicast_rendezvous_point_request import CreateNetworkSwitchRoutingMulticastRendezvousPointRequest
from openapi_server.models.create_network_switch_stack_routing_interface_request import CreateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server.models.get_device_switch_routing_interfaces200_response_inner import GetDeviceSwitchRoutingInterfaces200ResponseInner
from openapi_server.models.get_device_switch_routing_static_route200_response import GetDeviceSwitchRoutingStaticRoute200Response
from openapi_server.models.update_device_switch_routing_interface_dhcp_request import UpdateDeviceSwitchRoutingInterfaceDhcpRequest
from openapi_server.models.update_device_switch_routing_static_route_request import UpdateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.update_network_switch_routing_multicast_rendezvous_point_request import UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest
from openapi_server.models.update_network_switch_routing_multicast_request import UpdateNetworkSwitchRoutingMulticastRequest
from openapi_server.models.update_network_switch_routing_ospf_request import UpdateNetworkSwitchRoutingOspfRequest
from openapi_server.models.update_network_switch_stack_routing_interface_dhcp_request import UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest
from openapi_server.models.update_network_switch_stack_routing_interface_request import UpdateNetworkSwitchStackRoutingInterfaceRequest
from openapi_server import util


async def create_device_switch_routing_interface_1(request: web.Request, serial, body=None) -> web.Response:
    """Create a layer 3 interface for a switch

    Create a layer 3 interface for a switch

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_device_switch_routing_static_route_1(request: web.Request, serial, body) -> web.Response:
    """Create a layer 3 static route for a switch

    Create a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_routing_multicast_rendezvous_point_1(request: web.Request, network_id, body) -> web.Response:
    """Create a multicast rendezvous point

    Create a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchRoutingMulticastRendezvousPointRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_stack_routing_interface_2(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
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


async def create_network_switch_stack_routing_static_route_2(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
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


async def delete_device_switch_routing_interface_1(request: web.Request, serial, interface_id) -> web.Response:
    """Delete a layer 3 interface from the switch

    Delete a layer 3 interface from the switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def delete_device_switch_routing_static_route_1(request: web.Request, serial, static_route_id) -> web.Response:
    """Delete a layer 3 static route for a switch

    Delete a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_routing_multicast_rendezvous_point_1(request: web.Request, network_id, rendezvous_point_id) -> web.Response:
    """Delete a multicast rendezvous point

    Delete a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param rendezvous_point_id: 
    :type rendezvous_point_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_stack_routing_interface_2(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
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


async def delete_network_switch_stack_routing_static_route_2(request: web.Request, network_id, switch_stack_id, static_route_id) -> web.Response:
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


async def get_device_switch_routing_interface_1(request: web.Request, serial, interface_id) -> web.Response:
    """Return a layer 3 interface for a switch

    Return a layer 3 interface for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_interface_dhcp_1(request: web.Request, serial, interface_id) -> web.Response:
    """Return a layer 3 interface DHCP configuration for a switch

    Return a layer 3 interface DHCP configuration for a switch

    :param serial: 
    :type serial: str
    :param interface_id: 
    :type interface_id: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_interfaces_1(request: web.Request, serial) -> web.Response:
    """List layer 3 interfaces for a switch

    List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_static_route_1(request: web.Request, serial, static_route_id) -> web.Response:
    """Return a layer 3 static route for a switch

    Return a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_static_routes_1(request: web.Request, serial) -> web.Response:
    """List layer 3 static routes for a switch

    List layer 3 static routes for a switch

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_multicast_1(request: web.Request, network_id) -> web.Response:
    """Return multicast settings for a network

    Return multicast settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_multicast_rendezvous_point_1(request: web.Request, network_id, rendezvous_point_id) -> web.Response:
    """Return a multicast rendezvous point

    Return a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param rendezvous_point_id: 
    :type rendezvous_point_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_multicast_rendezvous_points_1(request: web.Request, network_id) -> web.Response:
    """List multicast rendezvous points

    List multicast rendezvous points

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_ospf_1(request: web.Request, network_id) -> web.Response:
    """Return layer 3 OSPF routing configuration

    Return layer 3 OSPF routing configuration

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_interface_2(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
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


async def get_network_switch_stack_routing_interface_dhcp_2(request: web.Request, network_id, switch_stack_id, interface_id) -> web.Response:
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


async def get_network_switch_stack_routing_interfaces_2(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """List layer 3 interfaces for a switch stack

    List layer 3 interfaces for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_static_route_2(request: web.Request, network_id, switch_stack_id, static_route_id) -> web.Response:
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


async def get_network_switch_stack_routing_static_routes_2(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """List layer 3 static routes for a switch stack

    List layer 3 static routes for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def update_device_switch_routing_interface_1(request: web.Request, serial, interface_id, body=None) -> web.Response:
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


async def update_device_switch_routing_interface_dhcp_1(request: web.Request, serial, interface_id, body=None) -> web.Response:
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


async def update_device_switch_routing_static_route_1(request: web.Request, serial, static_route_id, body=None) -> web.Response:
    """Update a layer 3 static route for a switch

    Update a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param static_route_id: 
    :type static_route_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceSwitchRoutingStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_routing_multicast_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update multicast settings for a network

    Update multicast settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchRoutingMulticastRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_routing_multicast_rendezvous_point_1(request: web.Request, network_id, rendezvous_point_id, body) -> web.Response:
    """Update a multicast rendezvous point

    Update a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param rendezvous_point_id: 
    :type rendezvous_point_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_routing_ospf_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update layer 3 OSPF routing configuration

    Update layer 3 OSPF routing configuration

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchRoutingOspfRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_interface_2(request: web.Request, network_id, switch_stack_id, interface_id, body=None) -> web.Response:
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


async def update_network_switch_stack_routing_interface_dhcp_2(request: web.Request, network_id, switch_stack_id, interface_id, body=None) -> web.Response:
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


async def update_network_switch_stack_routing_static_route_2(request: web.Request, network_id, switch_stack_id, static_route_id, body=None) -> web.Response:
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
