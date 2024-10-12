from typing import List, Dict
from aiohttp import web

from openapi_server.models.route import Route
from openapi_server.models.route_list_result import RouteListResult
from openapi_server import util


async def routes_create_or_update(request: web.Request, resource_group_name, route_table_name, route_name, api_version, subscription_id, route_parameters) -> web.Response:
    """routes_create_or_update

    The Put route operation creates/updates a route in the specified route table

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_table_name: The name of the route table.
    :type route_table_name: str
    :param route_name: The name of the route.
    :type route_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param route_parameters: Parameters supplied to the create/update route operation
    :type route_parameters: dict | bytes

    """
    route_parameters = Route.from_dict(route_parameters)
    return web.Response(status=200)


async def routes_delete(request: web.Request, resource_group_name, route_table_name, route_name, api_version, subscription_id) -> web.Response:
    """routes_delete

    The delete route operation deletes the specified route from a route table.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_table_name: The name of the route table.
    :type route_table_name: str
    :param route_name: The name of the route.
    :type route_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def routes_get(request: web.Request, resource_group_name, route_table_name, route_name, api_version, subscription_id) -> web.Response:
    """routes_get

    The Get route operation retrieves information about the specified route from the route table.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_table_name: The name of the route table.
    :type route_table_name: str
    :param route_name: The name of the route.
    :type route_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def routes_list(request: web.Request, resource_group_name, route_table_name, api_version, subscription_id) -> web.Response:
    """routes_list

    The List network security rule operation retrieves all the routes in a route table.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_table_name: The name of the route table.
    :type route_table_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
