from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.multi_route_result import MultiRouteResult
from openapi_server.models.route import Route
from openapi_server.models.route_create import RouteCreate
from openapi_server.models.route_result import RouteResult
from openapi_server import util


async def route_get(request: web.Request, filters=None) -> web.Response:
    """get routes

    Get a list of routes

    :param filters: A JSON encoded array of RouteFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any RouteFilter will be included. 
    :type filters: str

    """
    return web.Response(status=200)


async def route_post(request: web.Request, route) -> web.Response:
    """create route

    Create a new route

    :param route: the route to create
    :type route: dict | bytes

    """
    route = RouteCreate.from_dict(route)
    return web.Response(status=200)


async def route_route_key_delete(request: web.Request, route_key, checksum) -> web.Response:
    """delete route

    Delete an existing route

    :param route_key: the route key
    :type route_key: str
    :param checksum: the current checksum of the route to be deleted
    :type checksum: str

    """
    return web.Response(status=200)


async def route_route_key_get(request: web.Request, route_key) -> web.Response:
    """get route

    Get details for an existing route

    :param route_key: the route key
    :type route_key: str

    """
    return web.Response(status=200)


async def route_route_key_put(request: web.Request, route_key, route) -> web.Response:
    """modify route

    Modify an existing route

    :param route_key: the route key
    :type route_key: str
    :param route: the route to modify
    :type route: dict | bytes

    """
    route = Route.from_dict(route)
    return web.Response(status=200)


async def shared_rules_shared_rules_key_delete(request: web.Request, shared_rules_key, checksum) -> web.Response:
    """delete shared_rules object

    Delete an existing shared_rules object

    :param shared_rules_key: the shared_rules key
    :type shared_rules_key: str
    :param checksum: the current checksum of the shared_rules to be deleted
    :type checksum: str

    """
    return web.Response(status=200)
