from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.rule import Rule
from openapi_server.models.sb_subscription import SBSubscription
from openapi_server.models.sb_subscription_list_result import SBSubscriptionListResult
from openapi_server import util


async def rules_get(request: web.Request, resource_group_name, namespace_name, topic_name, subscription_name, rule_name, api_version, subscription_id) -> web.Response:
    """rules_get

    Retrieves the description for the specified rule.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param subscription_name: The subscription name.
    :type subscription_name: str
    :param rule_name: The rule name.
    :type rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


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
    parameters = SBSubscription.from_dict(parameters)
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


async def subscriptions_list_by_topic(request: web.Request, resource_group_name, namespace_name, topic_name, api_version, subscription_id, skip=None, top=None) -> web.Response:
    """subscriptions_list_by_topic

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
    :param skip: Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    :type skip: int
    :param top: May be used to limit the number of results to the most recent N usageDetails.
    :type top: int

    """
    return web.Response(status=200)
