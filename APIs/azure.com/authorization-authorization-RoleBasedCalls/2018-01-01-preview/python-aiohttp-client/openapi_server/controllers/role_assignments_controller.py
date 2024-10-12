from typing import List, Dict
from aiohttp import web

from openapi_server.models.role_assignment import RoleAssignment
from openapi_server.models.role_assignment_create_parameters import RoleAssignmentCreateParameters
from openapi_server.models.role_assignment_list_result import RoleAssignmentListResult
from openapi_server import util


async def role_assignments_create(request: web.Request, scope, role_assignment_name, api_version, parameters) -> web.Response:
    """role_assignments_create

    Creates a role assignment.

    :param scope: The scope of the role assignment to create. The scope can be any REST resource instance. For example, use &#39;/subscriptions/{subscription-id}/&#39; for a subscription, &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for a resource group, and &#39;/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}&#39; for a resource.
    :type scope: str
    :param role_assignment_name: The name of the role assignment to create. It can be any valid GUID.
    :type role_assignment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters for the role assignment.
    :type parameters: dict | bytes

    """
    parameters = RoleAssignmentCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def role_assignments_create_by_id(request: web.Request, role_id, api_version, parameters) -> web.Response:
    """role_assignments_create_by_id

    Creates a role assignment by ID.

    :param role_id: The ID of the role assignment to create.
    :type role_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters for the role assignment.
    :type parameters: dict | bytes

    """
    parameters = RoleAssignmentCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def role_assignments_delete(request: web.Request, scope, role_assignment_name, api_version) -> web.Response:
    """role_assignments_delete

    Deletes a role assignment.

    :param scope: The scope of the role assignment to delete.
    :type scope: str
    :param role_assignment_name: The name of the role assignment to delete.
    :type role_assignment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def role_assignments_delete_by_id(request: web.Request, role_id, api_version) -> web.Response:
    """role_assignments_delete_by_id

    Deletes a role assignment.

    :param role_id: The ID of the role assignment to delete.
    :type role_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def role_assignments_get(request: web.Request, scope, role_assignment_name, api_version) -> web.Response:
    """role_assignments_get

    Get the specified role assignment.

    :param scope: The scope of the role assignment.
    :type scope: str
    :param role_assignment_name: The name of the role assignment to get.
    :type role_assignment_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def role_assignments_get_by_id(request: web.Request, role_id, api_version) -> web.Response:
    """role_assignments_get_by_id

    Gets a role assignment by ID.

    :param role_id: The ID of the role assignment to get.
    :type role_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def role_assignments_list(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """role_assignments_list

    Gets all role assignments for the subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
    :type filter: str

    """
    return web.Response(status=200)


async def role_assignments_list_for_resource(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id, filter=None) -> web.Response:
    """role_assignments_list_for_resource

    Gets role assignments for a resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource identity.
    :type parent_resource_path: str
    :param resource_type: The resource type of the resource.
    :type resource_type: str
    :param resource_name: The name of the resource to get role assignments for.
    :type resource_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
    :type filter: str

    """
    return web.Response(status=200)


async def role_assignments_list_for_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, filter=None) -> web.Response:
    """role_assignments_list_for_resource_group

    Gets role assignments for a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
    :type filter: str

    """
    return web.Response(status=200)


async def role_assignments_list_for_scope(request: web.Request, scope, api_version, filter=None) -> web.Response:
    """role_assignments_list_for_scope

    Gets role assignments for a scope.

    :param scope: The scope of the role assignments.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter to apply on the operation. Use $filter&#x3D;atScope() to return all role assignments at or above the scope. Use $filter&#x3D;principalId eq {id} to return all role assignments at, above or below the scope for the specified principal.
    :type filter: str

    """
    return web.Response(status=200)
