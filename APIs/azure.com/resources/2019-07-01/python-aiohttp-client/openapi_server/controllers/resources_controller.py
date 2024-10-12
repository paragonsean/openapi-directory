from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.generic_resource import GenericResource
from openapi_server.models.resource_list_result import ResourceListResult
from openapi_server.models.resources_move_info import ResourcesMoveInfo
from openapi_server import util


async def resources_check_existence(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id) -> web.Response:
    """resources_check_existence

    Checks whether a resource exists.

    :param resource_group_name: The name of the resource group containing the resource to check. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: The resource provider of the resource to check.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type.
    :type resource_type: str
    :param resource_name: The name of the resource to check whether it exists.
    :type resource_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resources_check_existence_by_id(request: web.Request, resource_id, api_version) -> web.Response:
    """resources_check_existence_by_id

    Checks by ID whether a resource exists.

    :param resource_id: The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    :type resource_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def resources_create_or_update(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id, parameters) -> web.Response:
    """resources_create_or_update

    Creates a resource.

    :param resource_group_name: The name of the resource group for the resource. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type of the resource to create.
    :type resource_type: str
    :param resource_name: The name of the resource to create.
    :type resource_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters for creating or updating the resource.
    :type parameters: dict | bytes

    """
    parameters = GenericResource.from_dict(parameters)
    return web.Response(status=200)


async def resources_create_or_update_by_id(request: web.Request, resource_id, api_version, parameters) -> web.Response:
    """resources_create_or_update_by_id

    Create a resource by ID.

    :param resource_id: The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    :type resource_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param parameters: Create or update resource parameters.
    :type parameters: dict | bytes

    """
    parameters = GenericResource.from_dict(parameters)
    return web.Response(status=200)


async def resources_delete(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id) -> web.Response:
    """resources_delete

    Deletes a resource.

    :param resource_group_name: The name of the resource group that contains the resource to delete. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type.
    :type resource_type: str
    :param resource_name: The name of the resource to delete.
    :type resource_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resources_delete_by_id(request: web.Request, resource_id, api_version) -> web.Response:
    """resources_delete_by_id

    Deletes a resource by ID.

    :param resource_id: The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    :type resource_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def resources_get(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id) -> web.Response:
    """resources_get

    Gets a resource.

    :param resource_group_name: The name of the resource group containing the resource to get. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type of the resource.
    :type resource_type: str
    :param resource_name: The name of the resource to get.
    :type resource_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resources_get_by_id(request: web.Request, resource_id, api_version) -> web.Response:
    """resources_get_by_id

    Gets a resource by ID.

    :param resource_id: The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    :type resource_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def resources_list(request: web.Request, api_version, subscription_id, filter=None, expand=None, top=None) -> web.Response:
    """resources_list

    Get all the resources in a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.&lt;br&gt;&lt;br&gt;The properties you can use for eq (equals) or ne (not equals) are: location, resourceType, name, resourceGroup, identity, identity/principalId, plan, plan/publisher, plan/product, plan/name, plan/version, and plan/promotionCode.&lt;br&gt;&lt;br&gt;For example, to filter by a resource type, use: $filter&#x3D;resourceType eq &#39;Microsoft.Network/virtualNetworks&#39;&lt;br&gt;&lt;br&gt;You can use substringof(value, property) in the filter. The properties you can use for substring are: name and resourceGroup.&lt;br&gt;&lt;br&gt;For example, to get all resources with &#39;demo&#39; anywhere in the name, use: $filter&#x3D;substringof(&#39;demo&#39;, name)&lt;br&gt;&lt;br&gt;You can link more than one substringof together by adding and/or operators.&lt;br&gt;&lt;br&gt;You can filter by tag names and values. For example, to filter for a tag name and value, use $filter&#x3D;tagName eq &#39;tag1&#39; and tagValue eq &#39;Value1&#39;&lt;br&gt;&lt;br&gt;You can use some properties together when filtering. The combinations you can use are: substringof and/or resourceType, plan and plan/publisher and plan/name, identity and identity/principalId.
    :type filter: str
    :param expand: The $expand query parameter. You can expand createdTime and changedTime. For example, to expand both properties, use $expand&#x3D;changedTime,createdTime
    :type expand: str
    :param top: The number of results to return. If null is passed, returns all resource groups.
    :type top: int

    """
    return web.Response(status=200)


async def resources_move_resources(request: web.Request, source_resource_group_name, api_version, subscription_id, parameters) -> web.Response:
    """Moves resources from one resource group to another resource group.

    The resources to move must be in the same source resource group. The target resource group may be in a different subscription. When moving resources, both the source group and the target group are locked for the duration of the operation. Write and delete operations are blocked on the groups until the move completes. 

    :param source_resource_group_name: The name of the resource group containing the resources to move.
    :type source_resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters for moving resources.
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
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters for updating the resource.
    :type parameters: dict | bytes

    """
    parameters = GenericResource.from_dict(parameters)
    return web.Response(status=200)


async def resources_update_by_id(request: web.Request, resource_id, api_version, parameters) -> web.Response:
    """resources_update_by_id

    Updates a resource by ID.

    :param resource_id: The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
    :type resource_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param parameters: Update resource parameters.
    :type parameters: dict | bytes

    """
    parameters = GenericResource.from_dict(parameters)
    return web.Response(status=200)


async def resources_validate_move_resources(request: web.Request, source_resource_group_name, api_version, subscription_id, parameters) -> web.Response:
    """Validates whether resources can be moved from one resource group to another resource group.

    This operation checks whether the specified resources can be moved to the target. The resources to move must be in the same source resource group. The target resource group may be in a different subscription. If validation succeeds, it returns HTTP response code 204 (no content). If validation fails, it returns HTTP response code 409 (Conflict) with an error message. Retrieve the URL in the Location header value to check the result of the long-running operation.

    :param source_resource_group_name: The name of the resource group containing the resources to validate for move.
    :type source_resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters for moving resources.
    :type parameters: dict | bytes

    """
    parameters = ResourcesMoveInfo.from_dict(parameters)
    return web.Response(status=200)
