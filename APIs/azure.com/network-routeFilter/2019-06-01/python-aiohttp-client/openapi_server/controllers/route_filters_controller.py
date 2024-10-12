from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_route_filter import PatchRouteFilter
from openapi_server.models.route_filter import RouteFilter
from openapi_server.models.route_filter_list_result import RouteFilterListResult
from openapi_server import util


async def route_filters_create_or_update(request: web.Request, resource_group_name, route_filter_name, api_version, subscription_id, route_filter_parameters) -> web.Response:
    """route_filters_create_or_update

    Creates or updates a route filter in a specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_filter_name: The name of the route filter.
    :type route_filter_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param route_filter_parameters: Parameters supplied to the create or update route filter operation.
    :type route_filter_parameters: dict | bytes

    """
    route_filter_parameters = RouteFilter.from_dict(route_filter_parameters)
    return web.Response(status=200)


async def route_filters_delete(request: web.Request, resource_group_name, route_filter_name, api_version, subscription_id) -> web.Response:
    """route_filters_delete

    Deletes the specified route filter.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_filter_name: The name of the route filter.
    :type route_filter_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def route_filters_get(request: web.Request, resource_group_name, route_filter_name, api_version, subscription_id, expand=None) -> web.Response:
    """route_filters_get

    Gets the specified route filter.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_filter_name: The name of the route filter.
    :type route_filter_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced express route bgp peering resources.
    :type expand: str

    """
    return web.Response(status=200)


async def route_filters_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """route_filters_list

    Gets all route filters in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def route_filters_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """route_filters_list_by_resource_group

    Gets all route filters in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def route_filters_update(request: web.Request, resource_group_name, route_filter_name, api_version, subscription_id, route_filter_parameters) -> web.Response:
    """route_filters_update

    Updates a route filter in a specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_filter_name: The name of the route filter.
    :type route_filter_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param route_filter_parameters: Parameters supplied to the update route filter operation.
    :type route_filter_parameters: dict | bytes

    """
    route_filter_parameters = PatchRouteFilter.from_dict(route_filter_parameters)
    return web.Response(status=200)
