from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.scope_assignment import ScopeAssignment
from openapi_server.models.scope_assignment_list_result import ScopeAssignmentListResult
from openapi_server import util


async def scope_assignments_create_or_update(request: web.Request, scope, scope_assignment_name, api_version, parameters) -> web.Response:
    """scope_assignments_create_or_update

    Creates a scope assignment.

    :param scope: The base resource of the scope assignment to create. The scope can be any REST resource instance. For example, use &#39;subscriptions/{subscription-id}&#39; for a subscription, &#39;subscriptions/{subscription-id}/resourceGroups/{resource-group-name}&#39; for a resource group, and &#39;subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}&#39; for a resource.
    :type scope: str
    :param scope_assignment_name: The name of the scope assignment to create.
    :type scope_assignment_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: Parameters supplied to the specify which Managed Network this scope is being assigned
    :type parameters: dict | bytes

    """
    parameters = ScopeAssignment.from_dict(parameters)
    return web.Response(status=200)


async def scope_assignments_delete(request: web.Request, scope, scope_assignment_name, api_version) -> web.Response:
    """scope_assignments_delete

    Deletes a scope assignment.

    :param scope: The scope of the scope assignment to delete.
    :type scope: str
    :param scope_assignment_name: The name of the scope assignment to delete.
    :type scope_assignment_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def scope_assignments_get(request: web.Request, scope, scope_assignment_name, api_version) -> web.Response:
    """scope_assignments_get

    Get the specified scope assignment.

    :param scope: The base resource of the scope assignment.
    :type scope: str
    :param scope_assignment_name: The name of the scope assignment to get.
    :type scope_assignment_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def scope_assignments_list(request: web.Request, scope, api_version) -> web.Response:
    """scope_assignments_list

    Get the specified scope assignment.

    :param scope: The base resource of the scope assignment.
    :type scope: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
