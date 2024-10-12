from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.policy_assignment import PolicyAssignment
from openapi_server.models.policy_assignment_list_result import PolicyAssignmentListResult
from openapi_server import util


async def policy_assignments_create(request: web.Request, scope, policy_assignment_name, api_version, parameters) -> web.Response:
    """Creates or updates a policy assignment.

     This operation creates or updates a policy assignment with the given scope and name. Policy assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group.

    :param scope: The scope of the policy assignment. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39;
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
    """Creates or updates a policy assignment.

    This operation creates or updates the policy assignment with the given ID. Policy assignments made on a scope apply to all resources contained in that scope. For example, when you assign a policy to a resource group that policy applies to all resources in the group. Policy assignment IDs have this format: &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39;.

    :param policy_assignment_id: The ID of the policy assignment to create. Use the format &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;.
    :type policy_assignment_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param parameters: Parameters for policy assignment.
    :type parameters: dict | bytes

    """
    parameters = PolicyAssignment.from_dict(parameters)
    return web.Response(status=200)


async def policy_assignments_delete(request: web.Request, scope, policy_assignment_name, api_version) -> web.Response:
    """Deletes a policy assignment.

    This operation deletes a policy assignment, given its name and the scope it was created in. The scope of a policy assignment is the part of its ID preceding &#39;/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;.

    :param scope: The scope of the policy assignment. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39;
    :type scope: str
    :param policy_assignment_name: The name of the policy assignment to delete.
    :type policy_assignment_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_delete_by_id(request: web.Request, policy_assignment_id, api_version) -> web.Response:
    """Deletes a policy assignment.

    This operation deletes the policy with the given ID. Policy assignment IDs have this format: &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. Valid formats for {scope} are: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39; (management group), &#39;/subscriptions/{subscriptionId}&#39; (subscription), &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; (resource group), or &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39; (resource).

    :param policy_assignment_id: The ID of the policy assignment to delete. Use the format &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;.
    :type policy_assignment_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_get(request: web.Request, scope, policy_assignment_name, api_version) -> web.Response:
    """Retrieves a policy assignment.

    This operation retrieves a single policy assignment, given its name and the scope it was created at.

    :param scope: The scope of the policy assignment. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39;
    :type scope: str
    :param policy_assignment_name: The name of the policy assignment to get.
    :type policy_assignment_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_get_by_id(request: web.Request, policy_assignment_id, api_version) -> web.Response:
    """Retrieves the policy assignment with the given ID.

    The operation retrieves the policy assignment with the given ID. Policy assignment IDs have this format: &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;), resource group (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39;, or resource (format: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}&#39;.

    :param policy_assignment_id: The ID of the policy assignment to get. Use the format &#39;{scope}/providers/Microsoft.Authorization/policyAssignments/{policyAssignmentName}&#39;.
    :type policy_assignment_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_list(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """Retrieves all policy assignments that apply to a subscription.

    This operation retrieves the list of all policy assignments associated with the given subscription that match the optional given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, the unfiltered list includes all policy assignments associated with the subscription, including those that apply directly or from management groups that contain the given subscription, as well as any applied to objects contained within the subscription. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that apply to the subscription, which is everything in the unfiltered list except those applied to objects contained within the subscription. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value}.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, no filtering is performed.
    :type filter: str

    """
    return web.Response(status=200)


async def policy_assignments_list_for_management_group(request: web.Request, management_group_id, filter, api_version) -> web.Response:
    """Retrieves all policy assignments that apply to a management group.

    This operation retrieves the list of all policy assignments applicable to the management group that match the given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that are assigned to the management group or the management group&#39;s ancestors. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value} that apply to the management group.

    :param management_group_id: The ID of the management group.
    :type management_group_id: str
    :param filter: The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. A filter is required when listing policy assignments at management group scope.
    :type filter: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_list_for_resource(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id, filter=None) -> web.Response:
    """Retrieves all policy assignments that apply to a resource.

    This operation retrieves the list of all policy assignments associated with the specified resource in the given resource group and subscription that match the optional given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource, including those that apply directly or from all containing scopes, as well as any applied to resources contained within the resource. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that apply to the resource, which is everything in the unfiltered list except those applied to resources contained within the resource. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value} that apply to the resource. Three parameters plus the resource name are used to identify a specific resource. If the resource is not part of a parent resource (the more common case), the parent resource path should not be provided (or provided as &#39;&#39;). For example a web app could be specified as ({resourceProviderNamespace} &#x3D;&#x3D; &#39;Microsoft.Web&#39;, {parentResourcePath} &#x3D;&#x3D; &#39;&#39;, {resourceType} &#x3D;&#x3D; &#39;sites&#39;, {resourceName} &#x3D;&#x3D; &#39;MyWebApp&#39;). If the resource is part of a parent resource, then all parameters should be provided. For example a virtual machine DNS name could be specified as ({resourceProviderNamespace} &#x3D;&#x3D; &#39;Microsoft.Compute&#39;, {parentResourcePath} &#x3D;&#x3D; &#39;virtualMachines/MyVirtualMachine&#39;, {resourceType} &#x3D;&#x3D; &#39;domainNames&#39;, {resourceName} &#x3D;&#x3D; &#39;MyComputerName&#39;). A convenient alternative to providing the namespace and type name separately is to provide both in the {resourceType} parameter, format: ({resourceProviderNamespace} &#x3D;&#x3D; &#39;&#39;, {parentResourcePath} &#x3D;&#x3D; &#39;&#39;, {resourceType} &#x3D;&#x3D; &#39;Microsoft.Web/sites&#39;, {resourceName} &#x3D;&#x3D; &#39;MyWebApp&#39;).

    :param resource_group_name: The name of the resource group containing the resource.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider. For example, the namespace of a virtual machine is Microsoft.Compute (from Microsoft.Compute/virtualMachines)
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource path. Use empty string if there is none.
    :type parent_resource_path: str
    :param resource_type: The resource type name. For example the type name of a web app is &#39;sites&#39; (from Microsoft.Web/sites).
    :type resource_type: str
    :param resource_name: The name of the resource.
    :type resource_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, no filtering is performed.
    :type filter: str

    """
    return web.Response(status=200)


async def policy_assignments_list_for_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, filter=None) -> web.Response:
    """Retrieves all policy assignments that apply to a resource group.

    This operation retrieves the list of all policy assignments associated with the given resource group in the given subscription that match the optional given $filter. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, the unfiltered list includes all policy assignments associated with the resource group, including those that apply directly or apply from containing scopes, as well as any applied to resources contained within the resource group. If $filter&#x3D;atScope() is provided, the returned list includes all policy assignments that apply to the resource group, which is everything in the unfiltered list except those applied to resources contained within the resource group. If $filter&#x3D;policyDefinitionId eq &#39;{value}&#39; is provided, the returned list includes all policy assignments of the policy definition whose id is {value} that apply to the resource group.

    :param resource_group_name: The name of the resource group that contains policy assignments.
    :type resource_group_name: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. Valid values for $filter are: &#39;atScope()&#39; or &#39;policyDefinitionId eq &#39;{value}&#39;&#39;. If $filter is not provided, no filtering is performed.
    :type filter: str

    """
    return web.Response(status=200)
