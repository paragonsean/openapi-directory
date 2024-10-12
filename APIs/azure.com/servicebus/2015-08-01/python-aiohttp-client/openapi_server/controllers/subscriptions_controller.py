from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_create_or_update_parameters import SubscriptionCreateOrUpdateParameters
from openapi_server.models.subscription_list_result import SubscriptionListResult
from openapi_server.models.subscription_resource import SubscriptionResource
from openapi_server import util


async def subscriptions_create_or_update(request: web.Request, resource_group_name, namespace_name, topic_name, subscription_name, api_version, subscription_id, parameters) -> web.Response:
    """subscriptions_create_or_update

    Creates a topic subscription.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param subscription_name: The subscription name.
    :type subscription_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create a subscription resource.
    :type parameters: dict | bytes

    """
    parameters = SubscriptionCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def subscriptions_delete(request: web.Request, resource_group_name, namespace_name, topic_name, subscription_name, api_version, subscription_id) -> web.Response:
    """subscriptions_delete

    Deletes a subscription from the specified topic.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param subscription_name: The subscription name.
    :type subscription_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscriptions_get(request: web.Request, resource_group_name, namespace_name, topic_name, subscription_name, api_version, subscription_id) -> web.Response:
    """subscriptions_get

    Returns a subscription description for the specified topic.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param subscription_name: The subscription name.
    :type subscription_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscriptions_list_all(request: web.Request, resource_group_name, namespace_name, topic_name, api_version, subscription_id) -> web.Response:
    """subscriptions_list_all

    List all the subscriptions under a specified topic.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
