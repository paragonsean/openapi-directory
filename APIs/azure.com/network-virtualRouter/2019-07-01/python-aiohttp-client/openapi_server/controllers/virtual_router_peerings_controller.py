from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_router_peering import VirtualRouterPeering
from openapi_server.models.virtual_router_peering_list_result import VirtualRouterPeeringListResult
from openapi_server.models.virtual_routers_list_default_response import VirtualRoutersListDefaultResponse
from openapi_server import util


async def virtual_router_peerings_create_or_update(request: web.Request, resource_group_name, virtual_router_name, peering_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_router_peerings_create_or_update

    Creates or updates the specified Virtual Router Peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_router_name: The name of the Virtual Router.
    :type virtual_router_name: str
    :param peering_name: The name of the Virtual Router Peering.
    :type peering_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update Virtual Router Peering operation.
    :type parameters: dict | bytes

    """
    parameters = VirtualRouterPeering.from_dict(parameters)
    return web.Response(status=200)


async def virtual_router_peerings_delete(request: web.Request, resource_group_name, virtual_router_name, peering_name, api_version, subscription_id) -> web.Response:
    """virtual_router_peerings_delete

    Deletes the specified peering from a Virtual Router.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_router_name: The name of the Virtual Router.
    :type virtual_router_name: str
    :param peering_name: The name of the peering.
    :type peering_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_router_peerings_get(request: web.Request, resource_group_name, virtual_router_name, peering_name, api_version, subscription_id) -> web.Response:
    """virtual_router_peerings_get

    Gets the specified Virtual Router Peering.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param virtual_router_name: The name of the Virtual Router.
    :type virtual_router_name: str
    :param peering_name: The name of the Virtual Router Peering.
    :type peering_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_router_peerings_list(request: web.Request, resource_group_name, virtual_router_name, api_version, subscription_id) -> web.Response:
    """virtual_router_peerings_list

    Lists all Virtual Router Peerings in a Virtual Router resource.

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


async def virtual_router_peerings_update(request: web.Request, subscription_id, resource_group_name, virtual_router_name, api_version, peering_name, parameters) -> web.Response:
    """virtual_router_peerings_update

    Updates a Virtual Router Peering.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The resource group name of the Virtual Router Peering.
    :type resource_group_name: str
    :param virtual_router_name: The name of the Virtual Router.
    :type virtual_router_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param peering_name: The name of the Virtual Router Peering being updated.
    :type peering_name: str
    :param parameters: Parameters supplied to update Virtual Router Peering operation.
    :type parameters: dict | bytes

    """
    parameters = VirtualRouterPeering.from_dict(parameters)
    return web.Response(status=200)
