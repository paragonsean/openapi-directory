from typing import List, Dict
from aiohttp import web

from openapi_server.models.assignment import Assignment
from openapi_server.models.assignment_list import AssignmentList
from openapi_server import util


async def assignments_create_or_update(request: web.Request, api_version, scope, assignment_name, assignment) -> web.Response:
    """assignments_create_or_update

    Create or update a blueprint assignment.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param assignment_name: Name of the blueprint assignment.
    :type assignment_name: str
    :param assignment: Blueprint assignment object to save.
    :type assignment: dict | bytes

    """
    assignment = Assignment.from_dict(assignment)
    return web.Response(status=200)


async def assignments_delete(request: web.Request, api_version, scope, assignment_name) -> web.Response:
    """assignments_delete

    Delete a blueprint assignment.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param assignment_name: Name of the blueprint assignment.
    :type assignment_name: str

    """
    return web.Response(status=200)


async def assignments_get(request: web.Request, api_version, scope, assignment_name) -> web.Response:
    """assignments_get

    Get a blueprint assignment.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param assignment_name: Name of the blueprint assignment.
    :type assignment_name: str

    """
    return web.Response(status=200)


async def assignments_list(request: web.Request, api_version, scope) -> web.Response:
    """assignments_list

    List blueprint assignments within a subscription.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str

    """
    return web.Response(status=200)
