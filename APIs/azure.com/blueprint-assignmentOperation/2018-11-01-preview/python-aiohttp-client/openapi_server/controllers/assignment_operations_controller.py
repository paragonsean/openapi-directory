from typing import List, Dict
from aiohttp import web

from openapi_server.models.assignment_operation import AssignmentOperation
from openapi_server.models.assignment_operation_list import AssignmentOperationList
from openapi_server import util


async def assignment_operations_get(request: web.Request, api_version, scope, assignment_name, assignment_operation_name) -> web.Response:
    """assignment_operations_get

    Get a blueprint assignment operation.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param assignment_name: Name of the blueprint assignment.
    :type assignment_name: str
    :param assignment_operation_name: Name of the blueprint assignment operation.
    :type assignment_operation_name: str

    """
    return web.Response(status=200)


async def assignment_operations_list(request: web.Request, api_version, scope, assignment_name) -> web.Response:
    """assignment_operations_list

    List operations for given blueprint assignment within a subscription.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param assignment_name: Name of the blueprint assignment.
    :type assignment_name: str

    """
    return web.Response(status=200)
