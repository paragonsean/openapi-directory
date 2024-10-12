from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.registration_definition import RegistrationDefinition
from openapi_server.models.registration_definition_list import RegistrationDefinitionList
from openapi_server import util


async def registration_definitions_create_or_update(request: web.Request, registration_definition_id, api_version, scope, request_body) -> web.Response:
    """registration_definitions_create_or_update

    Creates or updates a registration definition.

    :param registration_definition_id: Guid of the registration definition.
    :type registration_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope: Scope of the resource.
    :type scope: str
    :param request_body: The parameters required to create new registration definition.
    :type request_body: dict | bytes

    """
    request_body = RegistrationDefinition.from_dict(request_body)
    return web.Response(status=200)


async def registration_definitions_delete(request: web.Request, registration_definition_id, api_version, scope) -> web.Response:
    """registration_definitions_delete

    Deletes the registration definition.

    :param registration_definition_id: Guid of the registration definition.
    :type registration_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope: Scope of the resource.
    :type scope: str

    """
    return web.Response(status=200)


async def registration_definitions_get(request: web.Request, scope, registration_definition_id, api_version) -> web.Response:
    """registration_definitions_get

    Gets the registration definition details.

    :param scope: Scope of the resource.
    :type scope: str
    :param registration_definition_id: Guid of the registration definition.
    :type registration_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def registration_definitions_list(request: web.Request, scope, api_version) -> web.Response:
    """registration_definitions_list

    Gets a list of the registration definitions.

    :param scope: Scope of the resource.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)
