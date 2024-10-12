from typing import List, Dict
from aiohttp import web

from openapi_server.models.delegated_providers_list200_response import DelegatedProvidersList200Response
from openapi_server.models.delegated_providers_list200_response_value_inner import DelegatedProvidersList200ResponseValueInner
from openapi_server import util


async def delegated_providers_get(request: web.Request, subscription_id, delegated_provider, api_version) -> web.Response:
    """delegated_providers_get

    Get the specified delegated provider.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param delegated_provider: DelegatedProvider identifier.
    :type delegated_provider: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delegated_providers_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """delegated_providers_list

    Get the list of delegatedProviders.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
