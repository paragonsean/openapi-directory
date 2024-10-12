from typing import List, Dict
from aiohttp import web

from openapi_server.models.role_definition import RoleDefinition
from openapi_server.models.role_definition_list_result import RoleDefinitionListResult
from openapi_server import util


async def role_definitions_create_or_update(request: web.Request, scope, role_definition_id, api_version, role_definition) -> web.Response:
    """role_definitions_create_or_update

    Creates or updates a role definition.

    :param scope: The scope of the role definition.
    :type scope: str
    :param role_definition_id: The ID of the role definition.
    :type role_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param role_definition: The values for the role definition.
    :type role_definition: dict | bytes

    """
    role_definition = RoleDefinition.from_dict(role_definition)
    return web.Response(status=200)


async def role_definitions_delete(request: web.Request, scope, role_definition_id, api_version) -> web.Response:
    """role_definitions_delete

    Deletes a role definition.

    :param scope: The scope of the role definition.
    :type scope: str
    :param role_definition_id: The ID of the role definition to delete.
    :type role_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def role_definitions_get(request: web.Request, scope, role_definition_id, api_version) -> web.Response:
    """role_definitions_get

    Get role definition by name (GUID).

    :param scope: The scope of the role definition.
    :type scope: str
    :param role_definition_id: The ID of the role definition.
    :type role_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def role_definitions_get_by_id(request: web.Request, role_definition_id, api_version) -> web.Response:
    """role_definitions_get_by_id

    Gets a role definition by ID.

    :param role_definition_id: The fully qualified role definition ID. Use the format, /subscriptions/{guid}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId} for subscription level role definitions, or /providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionId} for tenant level role definitions.
    :type role_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def role_definitions_list(request: web.Request, scope, api_version, filter=None) -> web.Response:
    """role_definitions_list

    Get all role definitions that are applicable at scope and above.

    :param scope: The scope of the role definition.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter to apply on the operation. Use atScopeAndBelow filter to search below the given scope as well.
    :type filter: str

    """
    return web.Response(status=200)
