from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_keys import AccessKeys
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.regenerate_access_key_parameters import RegenerateAccessKeyParameters
from openapi_server.models.sb_authorization_rule import SBAuthorizationRule
from openapi_server.models.sb_authorization_rule_list_result import SBAuthorizationRuleListResult
from openapi_server.models.sb_topic import SBTopic
from openapi_server.models.sb_topic_list_result import SBTopicListResult
from openapi_server import util


async def topics_create_or_update(request: web.Request, resource_group_name, namespace_name, topic_name, api_version, subscription_id, parameters) -> web.Response:
    """topics_create_or_update

    Creates a topic in the specified namespace.

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
    :param parameters: Parameters supplied to create a topic resource.
    :type parameters: dict | bytes

    """
    parameters = SBTopic.from_dict(parameters)
    return web.Response(status=200)


async def topics_create_or_update_authorization_rule(request: web.Request, resource_group_name, namespace_name, topic_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """topics_create_or_update_authorization_rule

    Creates an authorization rule for the specified topic.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The shared access authorization rule.
    :type parameters: dict | bytes

    """
    parameters = SBAuthorizationRule.from_dict(parameters)
    return web.Response(status=200)


async def topics_delete(request: web.Request, resource_group_name, namespace_name, topic_name, api_version, subscription_id) -> web.Response:
    """topics_delete

    Deletes a topic from the specified namespace and resource group.

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


async def topics_delete_authorization_rule(request: web.Request, resource_group_name, namespace_name, topic_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """topics_delete_authorization_rule

    Deletes a topic authorization rule.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def topics_get(request: web.Request, resource_group_name, namespace_name, topic_name, api_version, subscription_id) -> web.Response:
    """topics_get

    Returns a description for the specified topic.

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


async def topics_get_authorization_rule(request: web.Request, resource_group_name, namespace_name, topic_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """topics_get_authorization_rule

    Returns the specified authorization rule.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def topics_list_authorization_rules(request: web.Request, resource_group_name, namespace_name, topic_name, api_version, subscription_id) -> web.Response:
    """topics_list_authorization_rules

    Gets authorization rules for a topic.

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


async def topics_list_by_namespace(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, skip=None, top=None) -> web.Response:
    """topics_list_by_namespace

    Gets all the topics in a namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
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


async def topics_list_keys(request: web.Request, resource_group_name, namespace_name, topic_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """topics_list_keys

    Gets the primary and secondary connection strings for the topic.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def topics_regenerate_keys(request: web.Request, resource_group_name, namespace_name, topic_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """topics_regenerate_keys

    Regenerates primary or secondary connection strings for the topic.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param topic_name: The topic name.
    :type topic_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to regenerate the authorization rule.
    :type parameters: dict | bytes

    """
    parameters = RegenerateAccessKeyParameters.from_dict(parameters)
    return web.Response(status=200)
