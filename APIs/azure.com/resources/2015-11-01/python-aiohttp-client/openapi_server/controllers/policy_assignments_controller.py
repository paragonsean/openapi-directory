from typing import List, Dict
from aiohttp import web

from openapi_server.models.policy_assignment import PolicyAssignment
from openapi_server.models.policy_assignment_list_result import PolicyAssignmentListResult
from openapi_server import util


async def policy_assignments_create(request: web.Request, scope, policy_assignment_name, api_version, parameters) -> web.Response:
    """policy_assignments_create

    Create policy assignment.

    :param scope: Scope.
    :type scope: str
    :param policy_assignment_name: Policy assignment name.
    :type policy_assignment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Policy assignment.
    :type parameters: dict | bytes

    """
    parameters = PolicyAssignment.from_dict(parameters)
    return web.Response(status=200)


async def policy_assignments_create_by_id(request: web.Request, policy_assignment_id, api_version, parameters) -> web.Response:
    """policy_assignments_create_by_id

    Create policy assignment by Id.

    :param policy_assignment_id: Policy assignment Id
    :type policy_assignment_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Policy assignment.
    :type parameters: dict | bytes

    """
    parameters = PolicyAssignment.from_dict(parameters)
    return web.Response(status=200)


async def policy_assignments_delete(request: web.Request, scope, policy_assignment_name) -> web.Response:
    """policy_assignments_delete

    Delete policy assignment.

    :param scope: Scope.
    :type scope: str
    :param policy_assignment_name: Policy assignment name.
    :type policy_assignment_name: str

    """
    return web.Response(status=200)


async def policy_assignments_delete_by_id(request: web.Request, policy_assignment_id, api_version) -> web.Response:
    """policy_assignments_delete_by_id

    Delete policy assignment.

    :param policy_assignment_id: Policy assignment Id
    :type policy_assignment_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_get(request: web.Request, scope, policy_assignment_name, api_version) -> web.Response:
    """policy_assignments_get

    Get single policy assignment.

    :param scope: Scope.
    :type scope: str
    :param policy_assignment_name: Policy assignment name.
    :type policy_assignment_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_get_by_id(request: web.Request, policy_assignment_id, api_version) -> web.Response:
    """policy_assignments_get_by_id

    Get single policy assignment.

    :param policy_assignment_id: Policy assignment Id
    :type policy_assignment_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def policy_assignments_list(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """policy_assignments_list

    Gets policy assignments of the subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def policy_assignments_list_for_resource(request: web.Request, resource_group_name, resource_provider_namespace, parent_resource_path, resource_type, resource_name, api_version, subscription_id, filter=None) -> web.Response:
    """policy_assignments_list_for_resource

    Gets policy assignments of the resource.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_provider_namespace: The name of the resource provider.
    :type resource_provider_namespace: str
    :param parent_resource_path: The parent resource path.
    :type parent_resource_path: str
    :param resource_type: The resource type.
    :type resource_type: str
    :param resource_name: The resource name.
    :type resource_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def policy_assignments_list_for_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, filter=None) -> web.Response:
    """policy_assignments_list_for_resource_group

    Gets policy assignments of the resource group.

    :param resource_group_name: Resource group name.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def policy_assignments_list_for_scope(request: web.Request, scope, api_version, filter=None) -> web.Response:
    """policy_assignments_list_for_scope

    Gets policy assignments of the scope.

    :param scope: Scope.
    :type scope: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)
