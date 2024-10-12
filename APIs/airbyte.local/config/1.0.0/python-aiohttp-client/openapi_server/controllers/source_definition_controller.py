from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_source_definition_create import CustomSourceDefinitionCreate
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.private_source_definition_read import PrivateSourceDefinitionRead
from openapi_server.models.private_source_definition_read_list import PrivateSourceDefinitionReadList
from openapi_server.models.source_definition_id_request_body import SourceDefinitionIdRequestBody
from openapi_server.models.source_definition_id_with_workspace_id import SourceDefinitionIdWithWorkspaceId
from openapi_server.models.source_definition_read import SourceDefinitionRead
from openapi_server.models.source_definition_read_list import SourceDefinitionReadList
from openapi_server.models.source_definition_update import SourceDefinitionUpdate
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody
from openapi_server import util


async def create_custom_source_definition(request: web.Request, body=None) -> web.Response:
    """Creates a custom sourceDefinition for the given workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = CustomSourceDefinitionCreate.from_dict(body)
    return web.Response(status=200)


async def delete_source_definition(request: web.Request, body) -> web.Response:
    """Delete a source definition

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDefinitionIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_source_definition(request: web.Request, body) -> web.Response:
    """Get source

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDefinitionIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_source_definition_for_workspace(request: web.Request, body) -> web.Response:
    """Get a sourceDefinition that is configured for the given workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDefinitionIdWithWorkspaceId.from_dict(body)
    return web.Response(status=200)


async def grant_source_definition_to_workspace(request: web.Request, body) -> web.Response:
    """grant a private, non-custom sourceDefinition to a given workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDefinitionIdWithWorkspaceId.from_dict(body)
    return web.Response(status=200)


async def list_latest_source_definitions(request: web.Request, ) -> web.Response:
    """List the latest sourceDefinitions Airbyte supports

    Guaranteed to retrieve the latest information on supported sources.


    """
    return web.Response(status=200)


async def list_private_source_definitions(request: web.Request, body=None) -> web.Response:
    """List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def list_source_definitions(request: web.Request, ) -> web.Response:
    """List all the sourceDefinitions the current Airbyte deployment is configured to use

    


    """
    return web.Response(status=200)


async def list_source_definitions_for_workspace(request: web.Request, body=None) -> web.Response:
    """List all the sourceDefinitions the given workspace is configured to use

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def revoke_source_definition_from_workspace(request: web.Request, body) -> web.Response:
    """revoke a grant to a private, non-custom sourceDefinition from a given workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDefinitionIdWithWorkspaceId.from_dict(body)
    return web.Response(status=200)


async def update_source_definition(request: web.Request, body=None) -> web.Response:
    """Update a sourceDefinition

    

    :param body: 
    :type body: dict | bytes

    """
    body = SourceDefinitionUpdate.from_dict(body)
    return web.Response(status=200)
