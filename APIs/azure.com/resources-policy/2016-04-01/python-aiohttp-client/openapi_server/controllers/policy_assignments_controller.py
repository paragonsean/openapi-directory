from typing import List, Dict
from aiohttp import web

from openapi_server.models.policy_assignment import PolicyAssignment
from openapi_server.models.policy_assignment_list_result import PolicyAssignmentListResult
from openapi_server import util


async def policy_assignments_create(request: web.Request, scope, policy_assignment_name, api_version, parameters) -> web.Response:
    """Creates a policy assignment.

    Policy assignments are inherited by child resources. For example, when you apply a policy to a resource group that policy is assigned to all resources in the group.

    :param scope: The scope of the policy assignment.
    :type scope: str
    :param policy_assignment_name: The name of the policy assignment.
    :type policy_assignment_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param parameters: Parameters for the policy assignment.
    :type parameters: dict | bytes

    """
    parameters = PolicyAssignment.from_dict(parameters)
    return web.Response(status=200)


async def policy_assignments_create_by_id(request: web.Request, policy_assignment_id, api_version, parameters) -> web.Response:
    """Creates a policy assignment by ID.

    Policy assignments are inherited by child resources. For example, when you apply a policy to a resource group that policy is assigned to all resources in the group. When providing a scope for the assignment, use &#39;/subscriptions/{subscription-id}/&#39; for subscriptions, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for resource groups, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}&#39; for resources.

    :param policy_assignment_id: The ID of the policy assignment to create. Use the format &#39;/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}&#39;.
    :type policy_assignment_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param parameters: Parameters for policy assignment.
    :type parameters: dict | bytes

    """
    parameters = PolicyAssignment.from_dict(parameters)
    return web.Response(status=200)


async def policy_assignments_delete(request: web.Request, scope, policy_assignment_name, api_version) -> web.Response:
    """policy_assignments_delete

    Deletes a policy assignment.

    :param scope: The scope of the policy assignment.
    :type scope: str
    :param policy_assignment_name: The name of the policy assignment to delete.
    :type policy_assignment_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_delete_by_id(request: web.Request, policy_assignment_id, api_version) -> web.Response:
    """Deletes a policy assignment by ID.

    When providing a scope for the assignment, use &#39;/subscriptions/{subscription-id}/&#39; for subscriptions, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for resource groups, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}&#39; for resources.

    :param policy_assignment_id: The ID of the policy assignment to delete. Use the format &#39;/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}&#39;.
    :type policy_assignment_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_get(request: web.Request, scope, policy_assignment_name, api_version) -> web.Response:
    """policy_assignments_get

    Gets a policy assignment.

    :param scope: The scope of the policy assignment.
    :type scope: str
    :param policy_assignment_name: The name of the policy assignment to get.
    :type policy_assignment_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_get_by_id(request: web.Request, policy_assignment_id, api_version) -> web.Response:
    """Gets a policy assignment by ID.

    When providing a scope for the assignment, use &#39;/subscriptions/{subscription-id}/&#39; for subscriptions, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for resource groups, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}&#39; for resources.

    :param policy_assignment_id: The ID of the policy assignment to get. Use the format &#39;/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}&#39;.
    :type policy_assignment_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_list(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """policy_assignments_list

    Gets all the policy assignments for a subscription.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def policy_assignments_list_for_resource(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id, filter=None) -> web.Response:
    """policy_assignments_list_for_resource

    Gets policy assignments for a resource.

    :param resource_group_name: The name of the resource group containing the resource. The name is case insensitive.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource path.
    :type parent_resource_path: str
    :param resource_type: The resource type.
    :type resource_type: str
    :param resource_name: The name of the resource with policy assignments.
    :type resource_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def policy_assignments_list_for_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, filter=None) -> web.Response:
    """policy_assignments_list_for_resource_group

    Gets policy assignments for the resource group.

    :param resource_group_name: The name of the resource group that contains policy assignments.
    :type resource_group_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
