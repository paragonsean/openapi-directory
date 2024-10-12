from typing import List, Dict
from aiohttp import web

from openapi_server.models.provider import Provider
from openapi_server.models.provider_list_result import ProviderListResult
from openapi_server import util


async def providers_get(request: web.Request, resource_provider_namespace, api_version, subscription_id, expand=None) -> web.Response:
    """providers_get

    Gets a resource provider.

    :param resource_provider_namespace: Namespace of the resource provider.
    :type resource_provider_namespace: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: The $expand query parameter. e.g. To include property aliases in response, use $expand&#x3D;resourceTypes/aliases.
    :type expand: str

    """
    return web.Response(status=200)


async def providers_list(request: web.Request, api_version, subscription_id, top=None, expand=None) -> web.Response:
    """providers_list

    Gets a list of resource providers.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Query parameters. If null is passed returns all deployments.
    :type top: int
    :param expand: The $expand query parameter. e.g. To include property aliases in response, use $expand&#x3D;resourceTypes/aliases.
    :type expand: str

    """
    return web.Response(status=200)


async def providers_register(request: web.Request, resource_provider_namespace, api_version, subscription_id) -> web.Response:
    """providers_register

    Registers provider to be used with a subscription.

    :param resource_provider_namespace: Namespace of the resource provider.
    :type resource_provider_namespace: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def providers_unregister(request: web.Request, resource_provider_namespace, api_version, subscription_id) -> web.Response:
    """providers_unregister

    Unregisters provider from a subscription.

    :param resource_provider_namespace: Namespace of the resource provider.
    :type resource_provider_namespace: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
