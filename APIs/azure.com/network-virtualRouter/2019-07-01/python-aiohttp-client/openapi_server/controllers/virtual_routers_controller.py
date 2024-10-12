from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_router import VirtualRouter
from openapi_server.models.virtual_router_list_result import VirtualRouterListResult
from openapi_server.models.virtual_routers_list_default_response import VirtualRoutersListDefaultResponse
from openapi_server.models.virtual_routers_update_request import VirtualRoutersUpdateRequest
from openapi_server import util


async def virtual_routers_create_or_update(request: web.Request, resource_group_name, virtual_router_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_routers_create_or_update

    Creates or updates the specified Virtual Router.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_router_name: The name of the Virtual Router.
    :type virtual_router_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update Virtual Router.
    :type parameters: dict | bytes

    """
    parameters = VirtualRouter.from_dict(parameters)
    return web.Response(status=200)


async def virtual_routers_delete(request: web.Request, resource_group_name, virtual_router_name, api_version, subscription_id) -> web.Response:
    """virtual_routers_delete

    Deletes the specified Virtual Router.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_router_name: The name of the Virtual Router.
    :type virtual_router_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_routers_get(request: web.Request, resource_group_name, virtual_router_name, api_version, subscription_id, expand=None) -> web.Response:
    """virtual_routers_get

    Gets the specified Virtual Router.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_router_name: The name of the Virtual Router.
    :type virtual_router_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: Expands referenced resources.
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_routers_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """virtual_routers_list

    Gets all the Virtual Routers in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_routers_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """virtual_routers_list_by_resource_group

    Lists all Virtual Routers in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_routers_update(request: web.Request, subscription_id, resource_group_name, virtual_router_name, api_version, parameters) -> web.Response:
    """virtual_routers_update

    Updates a Virtual Router.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the Virtual Router.
    :type resource_group_name: str
    :param virtual_router_name: The name of the Virtual Router being updated.
    :type virtual_router_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param parameters: Parameters supplied to Update Virtual Router Tags.
    :type parameters: dict | bytes

    """
    parameters = VirtualRoutersUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
