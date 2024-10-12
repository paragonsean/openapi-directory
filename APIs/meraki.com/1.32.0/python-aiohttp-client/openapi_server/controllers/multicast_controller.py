from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_switch_routing_multicast_rendezvous_point_request import CreateNetworkSwitchRoutingMulticastRendezvousPointRequest
from openapi_server.models.update_network_switch_routing_multicast_rendezvous_point_request import UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest
from openapi_server.models.update_network_switch_routing_multicast_request import UpdateNetworkSwitchRoutingMulticastRequest
from openapi_server import util


async def create_network_switch_routing_multicast_rendezvous_point_2(request: web.Request, network_id, body) -> web.Response:
    """Create a multicast rendezvous point

    Create a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchRoutingMulticastRendezvousPointRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_switch_routing_multicast_rendezvous_point_2(request: web.Request, network_id, rendezvous_point_id) -> web.Response:
    """Delete a multicast rendezvous point

    Delete a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param rendezvous_point_id: 
    :type rendezvous_point_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_multicast_2(request: web.Request, network_id) -> web.Response:
    """Return multicast settings for a network

    Return multicast settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_multicast_rendezvous_point_2(request: web.Request, network_id, rendezvous_point_id) -> web.Response:
    """Return a multicast rendezvous point

    Return a multicast rendezvous point

    :param network_id: 
    :type network_id: str
    :param rendezvous_point_id: 
    :type rendezvous_point_id: str

    """
    return web.Response(status=200)


async def get_network_switch_routing_multicast_rendezvous_points_2(request: web.Request, network_id) -> web.Response:
    """List multicast rendezvous points

    List multicast rendezvous points

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_routing_multicast_2(request: web.Request, network_id, body=None) -> web.Response:
    """Update multicast settings for a network

    Update multicast settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchRoutingMulticastRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_switch_routing_multicast_rendezvous_point_2(request: web.Request, network_id, rendezvous_point_id, body) -> web.Response:
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
