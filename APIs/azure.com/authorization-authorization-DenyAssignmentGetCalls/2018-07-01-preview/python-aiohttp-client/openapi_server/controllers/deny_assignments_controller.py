from typing import List, Dict
from aiohttp import web

from openapi_server.models.deny_assignment import DenyAssignment
from openapi_server.models.deny_assignment_list_result import DenyAssignmentListResult
from openapi_server import util


async def deny_assignments_get(request: web.Request, scope, deny_assignment_id, api_version) -> web.Response:
    """deny_assignments_get

    Get the specified deny assignment.

    :param scope: The scope of the deny assignment.
    :type scope: str
    :param deny_assignment_id: The ID of the deny assignment to get.
    :type deny_assignment_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deny_assignments_get_by_id(request: web.Request, deny_assignment_id, api_version) -> web.Response:
    """deny_assignments_get_by_id

    Gets a deny assignment by ID.

    :param deny_assignment_id: The fully qualified deny assignment ID. For example, use the format, /subscriptions/{guid}/providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for subscription level deny assignments, or /providers/Microsoft.Authorization/denyAssignments/{denyAssignmentId} for tenant level deny assignments.
    :type deny_assignment_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def deny_assignments_list(request: web.Request, subscription_id, api_version, filter=None) -> web.Response:
    """deny_assignments_list

    Gets all deny assignments for the subscription.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
    :type filter: str

    """
    return web.Response(status=200)


async def deny_assignments_list_for_resource(request: web.Request, subscription_id, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, filter=None) -> web.Response:
    """deny_assignments_list_for_resource

    Gets deny assignments for a resource.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type of the resource.
    :type resource_type: str
    :param resource_name: The name of the resource to get deny assignments for.
    :type resource_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
    :type filter: str

    """
    return web.Response(status=200)


async def deny_assignments_list_for_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, filter=None) -> web.Response:
    """deny_assignments_list_for_resource_group

    Gets deny assignments for a resource group.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
    :type filter: str

    """
    return web.Response(status=200)


async def deny_assignments_list_for_scope(request: web.Request, scope, api_version, filter=None) -> web.Response:
    """deny_assignments_list_for_scope

    Gets deny assignments for a scope.

    :param scope: The scope of the deny assignments.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter to apply on the operation. Use $filter&#x3D;atScope() to return all deny assignments at or above the scope. Use $filter&#x3D;denyAssignmentName eq &#39;{name}&#39; to search deny assignments by name at specified scope. Use $filter&#x3D;principalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. Use $filter&#x3D;gdprExportPrincipalId eq &#39;{id}&#39; to return all deny assignments at, above and below the scope for the specified principal. This filter is different from the principalId filter as it returns not only those deny assignments that contain the specified principal is the Principals list but also those deny assignments that contain the specified principal is the ExcludePrincipals list. Additionally, when gdprExportPrincipalId filter is used, only the deny assignment name and description properties are returned.
    :type filter: str

    """
    return web.Response(status=200)
