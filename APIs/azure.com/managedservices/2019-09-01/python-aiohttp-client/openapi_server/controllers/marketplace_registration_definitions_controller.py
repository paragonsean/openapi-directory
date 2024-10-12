from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.marketplace_registration_definition_list import MarketplaceRegistrationDefinitionList
from openapi_server.models.registration_definition import RegistrationDefinition
from openapi_server import util


async def marketplace_registration_definitions_get(request: web.Request, scope, marketplace_identifier, api_version) -> web.Response:
    """marketplace_registration_definitions_get

    Get the marketplace registration definition for the marketplace identifier.

    :param scope: Scope of the resource.
    :type scope: str
    :param marketplace_identifier: Market place identifer. Expected Formats - {publisher}.{product[-preview]}.{planName}.{version} or {publisher}.{product[-preview]}.{planName} or {publisher}.{product[-preview]} or {publisher}).
    :type marketplace_identifier: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def marketplace_registration_definitions_list(request: web.Request, scope, api_version, filter=None) -> web.Response:
    """marketplace_registration_definitions_list

    Gets a list of the marketplace registration definitions for the marketplace identifier.

    :param scope: Scope of the resource.
    :type scope: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param filter: The filter query parameter. Might be used to filter marketplace registration definition by plan identifier, publisher, version etc.
    :type filter: str

    """
    return web.Response(status=200)
