from typing import List, Dict
from aiohttp import web

from openapi_server.models.feature_operations_list_result import FeatureOperationsListResult
from openapi_server.models.feature_result import FeatureResult
from openapi_server import util


async def features_get(request: web.Request, resource_provider_namespace, feature_name, api_version, subscription_id) -> web.Response:
    """features_get

    Gets the preview feature with the specified name.

    :param resource_provider_namespace: The resource provider namespace for the feature.
    :type resource_provider_namespace: str
    :param feature_name: The name of the feature to get.
    :type feature_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def features_list(request: web.Request, resource_provider_namespace, api_version, subscription_id) -> web.Response:
    """features_list

    Gets all the preview features in a provider namespace that are available through AFEC for the subscription.

    :param resource_provider_namespace: The namespace of the resource provider for getting features.
    :type resource_provider_namespace: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def features_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """features_list_all

    Gets all the preview features that are available through AFEC for the subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def features_register(request: web.Request, resource_provider_namespace, feature_name, api_version, subscription_id) -> web.Response:
    """features_register

    Registers the preview feature for the subscription.

    :param resource_provider_namespace: The namespace of the resource provider.
    :type resource_provider_namespace: str
    :param feature_name: The name of the feature to register.
    :type feature_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
