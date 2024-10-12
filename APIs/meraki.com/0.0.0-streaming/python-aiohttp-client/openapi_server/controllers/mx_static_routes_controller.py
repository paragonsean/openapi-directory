from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_static_route_request import CreateNetworkStaticRouteRequest
from openapi_server.models.update_network_static_route_request import UpdateNetworkStaticRouteRequest
from openapi_server import util


async def create_network_static_route(request: web.Request, network_id, body) -> web.Response:
    """Add a static route for an MX or teleworker network

    Add a static route for an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkStaticRouteRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_static_route(request: web.Request, network_id, static_route_id) -> web.Response:
    """Delete a static route from an MX or teleworker network

    Delete a static route from an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_network_static_route(request: web.Request, network_id, static_route_id) -> web.Response:
    """Return a static route for an MX or teleworker network

    Return a static route for an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param static_route_id: 
    :type static_route_id: str

    """
    return web.Response(status=200)


async def get_network_static_routes(request: web.Request, network_id) -> web.Response:
    """List the static routes for an MX or teleworker network

    List the static routes for an MX or teleworker network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_static_route(request: web.Request, network_id, static_route_id, body=None) -> web.Response:
    """Update a static route for an MX or teleworker network

    Update a static route for an MX or teleworker network

    :param network_id: 
    :type network_id: str
    :param static_route_id: 
    :type static_route_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkStaticRouteRequest.from_dict(body)
    return web.Response(status=200)
