from typing import List, Dict
from aiohttp import web

from openapi_server.models.generic_resource import GenericResource
from openapi_server.models.resource_list_result import ResourceListResult
from openapi_server.models.resources_move_info import ResourcesMoveInfo
from openapi_server import util


async def resources_check_existence(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id) -> web.Response:
    """resources_check_existence

    Checks whether resource exists.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: Resource identity.
    :type resource_provider_namespace: str
    :param parent_resource_path: Resource identity.
    :type parent_resource_path: str
    :param resource_type: Resource identity.
    :type resource_type: str
    :param resource_name: Resource identity.
    :type resource_name: str
    :param api_version: Api version to use.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resources_create_or_update(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id, parameters) -> web.Response:
    """resources_create_or_update

    Create a resource.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: Resource identity.
    :type resource_provider_namespace: str
    :param parent_resource_path: Resource identity.
    :type parent_resource_path: str
    :param resource_type: Resource identity.
    :type resource_type: str
    :param resource_name: Resource identity.
    :type resource_name: str
    :param api_version: Api version to use.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create or update resource parameters.
    :type parameters: dict | bytes

    """
    parameters = GenericResource.from_dict(parameters)
    return web.Response(status=200)


async def resources_delete(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id) -> web.Response:
    """resources_delete

    Delete resource and all of its resources. 

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: Resource identity.
    :type resource_provider_namespace: str
    :param parent_resource_path: Resource identity.
    :type parent_resource_path: str
    :param resource_type: Resource identity.
    :type resource_type: str
    :param resource_name: Resource identity.
    :type resource_name: str
    :param api_version: Api version to use.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resources_get(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id) -> web.Response:
    """resources_get

    Returns a resource belonging to a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: Resource identity.
    :type resource_provider_namespace: str
    :param parent_resource_path: Resource identity.
    :type parent_resource_path: str
    :param resource_type: Resource identity.
    :type resource_type: str
    :param resource_name: Resource identity.
    :type resource_name: str
    :param api_version: Api version to use.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resources_list(request: web.Request, api_version, subscription_id, filter=None, expand=None, top=None) -> web.Response:
    """resources_list

    Get all of the resources under a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param expand: The $expand query parameter.
    :type expand: str
    :param top: Query parameters. If null is passed returns all resource groups.
    :type top: int

    """
    return web.Response(status=200)


async def resources_move_resources(request: web.Request, source_resource_group_name, api_version, subscription_id, parameters) -> web.Response:
    """resources_move_resources

    Move resources from one resource group to another. The resources being moved should all be in the same resource group.

    :param source_resource_group_name: Source resource group name.
    :type source_resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: move resources&#39; parameters.
    :type parameters: dict | bytes

    """
    parameters = ResourcesMoveInfo.from_dict(parameters)
    return web.Response(status=200)


async def resources_update(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id, parameters) -> web.Response:
    """resources_update

    Updates a resource.

    :param resource_group_name: The name of the resource group for the resource. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type of the resource to update.
    :type resource_type: str
    :param resource_name: The name of the resource to update.
    :type resource_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters for updating the resource.
    :type parameters: dict | bytes

    """
    parameters = GenericResource.from_dict(parameters)
    return web.Response(status=200)
