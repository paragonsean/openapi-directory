from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_keys import AccessKeys
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.regenerate_access_key_parameters import RegenerateAccessKeyParameters
from openapi_server.models.sb_authorization_rule import SBAuthorizationRule
from openapi_server.models.sb_authorization_rule_list_result import SBAuthorizationRuleListResult
from openapi_server.models.sb_queue import SBQueue
from openapi_server.models.sb_queue_list_result import SBQueueListResult
from openapi_server import util


async def queues_create_or_update(request: web.Request, resource_group_name, namespace_name, queue_name, api_version, subscription_id, parameters) -> web.Response:
    """queues_create_or_update

    Creates or updates a Service Bus queue. This operation is idempotent.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param queue_name: The queue name.
    :type queue_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create or update a queue resource.
    :type parameters: dict | bytes

    """
    parameters = SBQueue.from_dict(parameters)
    return web.Response(status=200)


async def queues_create_or_update_authorization_rule(request: web.Request, resource_group_name, namespace_name, queue_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """queues_create_or_update_authorization_rule

    Creates an authorization rule for a queue.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param queue_name: The queue name.
    :type queue_name: str
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


async def queues_delete(request: web.Request, resource_group_name, namespace_name, queue_name, api_version, subscription_id) -> web.Response:
    """queues_delete

    Deletes a queue from the specified namespace in a resource group.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param queue_name: The queue name.
    :type queue_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def queues_delete_authorization_rule(request: web.Request, resource_group_name, namespace_name, queue_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """queues_delete_authorization_rule

    Deletes a queue authorization rule.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param queue_name: The queue name.
    :type queue_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def queues_get(request: web.Request, resource_group_name, namespace_name, queue_name, api_version, subscription_id) -> web.Response:
    """queues_get

    Returns a description for the specified queue.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param queue_name: The queue name.
    :type queue_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def queues_get_authorization_rule(request: web.Request, resource_group_name, namespace_name, queue_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """queues_get_authorization_rule

    Gets an authorization rule for a queue by rule name.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param queue_name: The queue name.
    :type queue_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def queues_list_authorization_rules(request: web.Request, resource_group_name, namespace_name, queue_name, api_version, subscription_id) -> web.Response:
    """queues_list_authorization_rules

    Gets all authorization rules for a queue.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param queue_name: The queue name.
    :type queue_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def queues_list_by_namespace(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, skip=None, top=None) -> web.Response:
    """queues_list_by_namespace

    Gets the queues within a namespace.

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


async def queues_list_keys(request: web.Request, resource_group_name, namespace_name, queue_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """queues_list_keys

    Primary and secondary connection strings to the queue.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param queue_name: The queue name.
    :type queue_name: str
    :param authorization_rule_name: The authorization rule name.
    :type authorization_rule_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def queues_regenerate_keys(request: web.Request, resource_group_name, namespace_name, queue_name, authorization_rule_name, api_version, subscription_id, parameters) -> web.Response:
    """queues_regenerate_keys

    Regenerates the primary or secondary connection strings to the queue.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param queue_name: The queue name.
    :type queue_name: str
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
