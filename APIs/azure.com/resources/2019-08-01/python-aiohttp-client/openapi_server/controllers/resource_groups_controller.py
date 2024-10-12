from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.export_template_request import ExportTemplateRequest
from openapi_server.models.resource_group import ResourceGroup
from openapi_server.models.resource_group_export_result import ResourceGroupExportResult
from openapi_server.models.resource_group_list_result import ResourceGroupListResult
from openapi_server.models.resource_group_patchable import ResourceGroupPatchable
from openapi_server.models.resource_list_result import ResourceListResult
from openapi_server import util


async def resource_groups_check_existence(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """resource_groups_check_existence

    Checks whether a resource group exists.

    :param resource_group_name: The name of the resource group to check. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resource_groups_create_or_update(request: web.Request, resource_group_name, api_version, subscription_id, parameters) -> web.Response:
    """resource_groups_create_or_update

    Creates or updates a resource group.

    :param resource_group_name: The name of the resource group to create or update. Can include alphanumeric, underscore, parentheses, hyphen, period (except at end), and Unicode characters that match the allowed characters.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update a resource group.
    :type parameters: dict | bytes

    """
    parameters = ResourceGroup.from_dict(parameters)
    return web.Response(status=200)


async def resource_groups_delete(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """Deletes a resource group.

    When you delete a resource group, all of its resources are also deleted. Deleting a resource group deletes all of its template deployments and currently stored operations.

    :param resource_group_name: The name of the resource group to delete. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resource_groups_export_template(request: web.Request, subscription_id, resource_group_name, api_version, parameters) -> web.Response:
    """resource_groups_export_template

    Captures the specified resource group as a template.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters for exporting the template.
    :type parameters: dict | bytes

    """
    parameters = ExportTemplateRequest.from_dict(parameters)
    return web.Response(status=200)


async def resource_groups_get(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """resource_groups_get

    Gets a resource group.

    :param resource_group_name: The name of the resource group to get. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def resource_groups_list(request: web.Request, api_version, subscription_id, filter=None, top=None) -> web.Response:
    """resource_groups_list

    Gets all the resource groups for a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.&lt;br&gt;&lt;br&gt;You can filter by tag names and values. For example, to filter for a tag name and value, use $filter&#x3D;tagName eq &#39;tag1&#39; and tagValue eq &#39;Value1&#39;
    :type filter: str
    :param top: The number of results to return. If null is passed, returns all resource groups.
    :type top: int

    """
    return web.Response(status=200)


async def resource_groups_update(request: web.Request, resource_group_name, api_version, subscription_id, parameters) -> web.Response:
    """Updates a resource group.

    Resource groups can be updated through a simple PATCH operation to a group address. The format of the request is the same as that for creating a resource group. If a field is unspecified, the current value is retained.

    :param resource_group_name: The name of the resource group to update. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to update a resource group.
    :type parameters: dict | bytes

    """
    parameters = ResourceGroupPatchable.from_dict(parameters)
    return web.Response(status=200)


async def resources_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, filter=None, expand=None, top=None) -> web.Response:
    """resources_list_by_resource_group

    Get all the resources for a resource group.

    :param resource_group_name: The resource group with the resources to get.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.&lt;br&gt;&lt;br&gt;The properties you can use for eq (equals) or ne (not equals) are: location, resourceType, name, resourceGroup, identity, identity/principalId, plan, plan/publisher, plan/product, plan/name, plan/version, and plan/promotionCode.&lt;br&gt;&lt;br&gt;For example, to filter by a resource type, use: $filter&#x3D;resourceType eq &#39;Microsoft.Network/virtualNetworks&#39;&lt;br&gt;&lt;br&gt;You can use substringof(value, property) in the filter. The properties you can use for substring are: name and resourceGroup.&lt;br&gt;&lt;br&gt;For example, to get all resources with &#39;demo&#39; anywhere in the name, use: $filter&#x3D;substringof(&#39;demo&#39;, name)&lt;br&gt;&lt;br&gt;You can link more than one substringof together by adding and/or operators.&lt;br&gt;&lt;br&gt;You can filter by tag names and values. For example, to filter for a tag name and value, use $filter&#x3D;tagName eq &#39;tag1&#39; and tagValue eq &#39;Value1&#39;. When you filter by a tag name and value, the tags for each resource are not returned in the results.&lt;br&gt;&lt;br&gt;You can use some properties together when filtering. The combinations you can use are: substringof and/or resourceType, plan and plan/publisher and plan/name, identity and identity/principalId.
    :type filter: str
    :param expand: The $expand query parameter. You can expand createdTime and changedTime. For example, to expand both properties, use $expand&#x3D;changedTime,createdTime
    :type expand: str
    :param top: The number of results to return. If null is passed, returns all resources.
    :type top: int

    """
    return web.Response(status=200)
