from typing import List, Dict
from aiohttp import web

from openapi_server.models.regenerate_keys_parameters import RegenerateKeysParameters
from openapi_server.models.resource_list_keys import ResourceListKeys
from openapi_server.models.shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource
from openapi_server.models.topic_create_or_update_parameters import TopicCreateOrUpdateParameters
from openapi_server.models.topic_list_result import TopicListResult
from openapi_server.models.topic_resource import TopicResource
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
    parameters = TopicCreateOrUpdateParameters.from_dict(parameters)
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
    parameters = SharedAccessAuthorizationRuleCreateOrUpdateParameters.from_dict(parameters)
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


async def topics_list_all(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """topics_list_all

    Gets all the topics in a namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
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


async def topics_post_authorization_rule(request: web.Request, resource_group_name, namespace_name, topic_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """topics_post_authorization_rule

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
    parameters = RegenerateKeysParameters.from_dict(parameters)
    return web.Response(status=200)
