from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_device_switch_routing_static_route_request import CreateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.create_network_appliance_static_route_request import CreateNetworkApplianceStaticRouteRequest
from openapi_server.models.get_device_switch_routing_static_route200_response import GetDeviceSwitchRoutingStaticRoute200Response
from openapi_server.models.update_device_switch_routing_static_route_request import UpdateDeviceSwitchRoutingStaticRouteRequest
from openapi_server.models.update_network_appliance_static_route_request import UpdateNetworkApplianceStaticRouteRequest
from openapi_server import util


async def create_device_switch_routing_static_route_2(request: web.Request, serial, body) -> web.Response:
    """Create a layer 3 static route for a switch

    Create a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceSwitchRoutingStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_appliance_static_route_1(request: web.Request, network_id, body) -> web.Response:
    """Add a static route for an MX or teleworker network

    Add a static route for an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkApplianceStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_switch_stack_routing_static_route_3(request: web.Request, network_id, switch_stack_id, body) -> web.Response:
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


async def delete_device_switch_routing_static_route_2(request: web.Request, serial, static_route_id) -> web.Response:
    """Delete a layer 3 static route for a switch

    Delete a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def delete_network_appliance_static_route_1(request: web.Request, network_id, static_route_id) -> web.Response:
    """Delete a static route from an MX or teleworker network

    Delete a static route from an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def delete_network_switch_stack_routing_static_route_3(request: web.Request, network_id, switch_stack_id, static_route_id) -> web.Response:
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


async def get_device_switch_routing_static_route_2(request: web.Request, serial, static_route_id) -> web.Response:
    """Return a layer 3 static route for a switch

    Return a layer 3 static route for a switch

    :param serial: 
    :type serial: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_device_switch_routing_static_routes_2(request: web.Request, serial) -> web.Response:
    """List layer 3 static routes for a switch

    List layer 3 static routes for a switch

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_appliance_static_route_1(request: web.Request, network_id, static_route_id) -> web.Response:
    """Return a static route for an MX or teleworker network

    Return a static route for an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_static_routes_1(request: web.Request, network_id) -> web.Response:
    """List the static routes for an MX or teleworker network

    List the static routes for an MX or teleworker network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_stack_routing_static_route_3(request: web.Request, network_id, switch_stack_id, static_route_id) -> web.Response:
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


async def get_network_switch_stack_routing_static_routes_3(request: web.Request, network_id, switch_stack_id) -> web.Response:
    """List layer 3 static routes for a switch stack

    List layer 3 static routes for a switch stack

    :param network_id: 
    :type network_id: str
    :param switch_stack_id: 
    :type switch_stack_id: str

    """
    return web.Response(status=200)


async def update_device_switch_routing_static_route_2(request: web.Request, serial, static_route_id, body=None) -> web.Response:
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


async def update_network_appliance_static_route_1(request: web.Request, network_id, static_route_id, body=None) -> web.Response:
    """Update a static route for an MX or teleworker network

    Update a static route for an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param static_route_id: 
    :type static_route_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_stack_routing_static_route_3(request: web.Request, network_id, switch_stack_id, static_route_id, body=None) -> web.Response:
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
