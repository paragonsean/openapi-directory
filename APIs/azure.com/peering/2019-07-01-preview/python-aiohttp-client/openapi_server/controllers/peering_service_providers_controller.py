from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_service_provider_list_result import PeeringServiceProviderListResult
from openapi_server import util


async def peering_service_providers_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """peering_service_providers_list

    Lists all of the available peering service locations for the specified kind of peering.

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
