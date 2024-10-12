from typing import List, Dict
from aiohttp import web

from openapi_server.models.provider import Provider
from openapi_server.models.provider_list_result import ProviderListResult
from openapi_server import util


async def providers_get(request: web.Request, resource_provider_namespace, api_version, subscription_id, expand=None) -> web.Response:
    """providers_get

    Gets the specified resource provider.

    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param expand: The $expand query parameter. For example, to include property aliases in response, use $expand&#x3D;resourceTypes/aliases.
    :type expand: str

    """
    return web.Response(status=200)


async def providers_list(request: web.Request, api_version, subscription_id, top=None, expand=None) -> web.Response:
    """providers_list

    Gets all resource providers for a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param top: The number of results to return. If null is passed returns all deployments.
    :type top: int
    :param expand: The properties to include in the results. For example, use &amp;$expand&#x3D;metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand&#x3D;resourceTypes/aliases.
    :type expand: str

    """
    return web.Response(status=200)


async def providers_register(request: web.Request, resource_provider_namespace, api_version, subscription_id) -> web.Response:
    """providers_register

    Registers a subscription with a resource provider.

    :param resource_provider_namespace: The namespace of the resource provider to register.
    :type resource_provider_namespace: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def providers_unregister(request: web.Request, resource_provider_namespace, api_version, subscription_id) -> web.Response:
    """providers_unregister

    Unregisters a subscription from a resource provider.

    :param resource_provider_namespace: The namespace of the resource provider to unregister.
    :type resource_provider_namespace: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
