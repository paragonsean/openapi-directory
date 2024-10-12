from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_destination_definition_create import CustomDestinationDefinitionCreate
from openapi_server.models.destination_definition_id_request_body import DestinationDefinitionIdRequestBody
from openapi_server.models.destination_definition_id_with_workspace_id import DestinationDefinitionIdWithWorkspaceId
from openapi_server.models.destination_definition_read import DestinationDefinitionRead
from openapi_server.models.destination_definition_read_list import DestinationDefinitionReadList
from openapi_server.models.destination_definition_update import DestinationDefinitionUpdate
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.private_destination_definition_read import PrivateDestinationDefinitionRead
from openapi_server.models.private_destination_definition_read_list import PrivateDestinationDefinitionReadList
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody
from openapi_server import util


async def create_custom_destination_definition(request: web.Request, body=None) -> web.Response:
    """Creates a custom destinationDefinition for the given workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = CustomDestinationDefinitionCreate.from_dict(body)
    return web.Response(status=200)


async def delete_destination_definition(request: web.Request, body) -> web.Response:
    """Delete a destination definition

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationDefinitionIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_destination_definition(request: web.Request, body) -> web.Response:
    """Get destinationDefinition

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationDefinitionIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_destination_definition_for_workspace(request: web.Request, body) -> web.Response:
    """Get a destinationDefinition that is configured for the given workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationDefinitionIdWithWorkspaceId.from_dict(body)
    return web.Response(status=200)


async def grant_destination_definition_to_workspace(request: web.Request, body) -> web.Response:
    """grant a private, non-custom destinationDefinition to a given workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationDefinitionIdWithWorkspaceId.from_dict(body)
    return web.Response(status=200)


async def list_destination_definitions(request: web.Request, ) -> web.Response:
    """List all the destinationDefinitions the current Airbyte deployment is configured to use

    


    """
    return web.Response(status=200)


async def list_destination_definitions_for_workspace(request: web.Request, body=None) -> web.Response:
    """List all the destinationDefinitions the given workspace is configured to use

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def list_latest_destination_definitions(request: web.Request, ) -> web.Response:
    """List the latest destinationDefinitions Airbyte supports

    Guaranteed to retrieve the latest information on supported destinations.


    """
    return web.Response(status=200)


async def list_private_destination_definitions(request: web.Request, body=None) -> web.Response:
    """List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.

    

    :param body: 
    :type body: dict | bytes

    """
    body = WorkspaceIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def revoke_destination_definition_from_workspace(request: web.Request, body) -> web.Response:
    """revoke a grant to a private, non-custom destinationDefinition from a given workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationDefinitionIdWithWorkspaceId.from_dict(body)
    return web.Response(status=200)


async def update_destination_definition(request: web.Request, body) -> web.Response:
    """Update destinationDefinition

    

    :param body: 
    :type body: dict | bytes

    """
    body = DestinationDefinitionUpdate.from_dict(body)
    return web.Response(status=200)
