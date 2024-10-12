from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.service_provider_response_list import ServiceProviderResponseList
from openapi_server import util


async def bot_connection_list_service_providers(request: web.Request, api_version, subscription_id) -> web.Response:
    """bot_connection_list_service_providers

    Lists the available Service Providers for creating Connection Settings

    :param api_version: Version of the API to be used with the client request. Current version is 2017-12-01
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)
