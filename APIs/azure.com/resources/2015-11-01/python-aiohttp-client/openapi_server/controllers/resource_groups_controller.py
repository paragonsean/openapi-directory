from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_group import ResourceGroup
from openapi_server.models.resource_group_list_result import ResourceGroupListResult
from openapi_server.models.resource_list_result import ResourceListResult
from openapi_server import util


async def resource_groups_check_existence(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """resource_groups_check_existence

    Checks whether resource group exists.

    :param resource_group_name: The name of the resource group to check. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resource_groups_create_or_update(request: web.Request, resource_group_name, api_version, subscription_id, parameters) -> web.Response:
    """resource_groups_create_or_update

    Create a resource group.

    :param resource_group_name: The name of the resource group to be created or updated.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update resource group service operation.
    :type parameters: dict | bytes

    """
    parameters = ResourceGroup.from_dict(parameters)
    return web.Response(status=200)


async def resource_groups_delete(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """resource_groups_delete

    Begin deleting resource group.To determine whether the operation has finished processing the request, call GetLongRunningOperationStatus.

    :param resource_group_name: The name of the resource group to be deleted. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resource_groups_get(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """resource_groups_get

    Get a resource group.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resource_groups_list(request: web.Request, api_version, subscription_id, filter=None, top=None) -> web.Response:
    """resource_groups_list

    Gets a collection of resource groups.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: Query parameters. If null is passed returns all resource groups.
    :type top: int

    """
    return web.Response(status=200)


async def resource_groups_list_resources(request: web.Request, resource_group_name, api_version, subscription_id, filter=None, top=None) -> web.Response:
    """resource_groups_list_resources

    Get all of the resources under a subscription.

    :param resource_group_name: Query parameters. If null is passed returns all resource groups.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: Query parameters. If null is passed returns all resource groups.
    :type top: int

    """
    return web.Response(status=200)


async def resource_groups_patch(request: web.Request, resource_group_name, api_version, subscription_id, parameters) -> web.Response:
    """resource_groups_patch

    Resource groups can be updated through a simple PATCH operation to a group address. The format of the request is the same as that for creating a resource groups, though if a field is unspecified current value will be carried over. 

    :param resource_group_name: The name of the resource group to be created or updated. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the update state resource group service operation.
    :type parameters: dict | bytes

    """
    parameters = ResourceGroup.from_dict(parameters)
    return web.Response(status=200)
