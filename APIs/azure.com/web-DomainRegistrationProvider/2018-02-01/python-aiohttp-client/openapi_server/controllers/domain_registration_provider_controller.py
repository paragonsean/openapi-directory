from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain_registration_provider_list_operations200_response import DomainRegistrationProviderListOperations200Response
from openapi_server.models.domain_registration_provider_list_operations_default_response import DomainRegistrationProviderListOperationsDefaultResponse
from openapi_server import util


async def domain_registration_provider_list_operations(request: web.Request, api_version) -> web.Response:
    """Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider

    Implements Csm operations Api to exposes the list of available Csm Apis under the resource provider

    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
