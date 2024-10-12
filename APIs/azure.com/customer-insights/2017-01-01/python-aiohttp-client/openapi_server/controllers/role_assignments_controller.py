from typing import List, Dict
from aiohttp import web

from openapi_server.models.role_assignment_list_result import RoleAssignmentListResult
from openapi_server.models.role_assignment_resource_format import RoleAssignmentResourceFormat
from openapi_server import util


async def role_assignments_create_or_update(request: web.Request, resource_group_name, hub_name, assignment_name, api_version, subscription_id, parameters) -> web.Response:
    """role_assignments_create_or_update

    Creates or updates a role assignment in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param assignment_name: The assignment name
    :type assignment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate RoleAssignment operation.
    :type parameters: dict | bytes

    """
    parameters = RoleAssignmentResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def role_assignments_delete(request: web.Request, resource_group_name, hub_name, assignment_name, api_version, subscription_id) -> web.Response:
    """role_assignments_delete

    Deletes the role assignment in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param assignment_name: The name of the role assignment.
    :type assignment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def role_assignments_get(request: web.Request, resource_group_name, hub_name, assignment_name, api_version, subscription_id) -> web.Response:
    """role_assignments_get

    Gets the role assignment in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param assignment_name: The name of the role assignment.
    :type assignment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def role_assignments_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """role_assignments_list_by_hub

    Gets all the role assignments for the specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
