from typing import List, Dict
from aiohttp import web

from openapi_server.models.queue_create_or_update_parameters import QueueCreateOrUpdateParameters
from openapi_server.models.queue_list_result import QueueListResult
from openapi_server.models.queue_resource import QueueResource
from openapi_server.models.shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
from openapi_server.models.shared_access_authorization_rule_get_resource import SharedAccessAuthorizationRuleGetResource
from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource
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
    parameters = QueueCreateOrUpdateParameters.from_dict(parameters)
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
    parameters = SharedAccessAuthorizationRuleCreateOrUpdateParameters.from_dict(parameters)
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


async def queues_list_all(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """queues_list_all

    Gets the queues within a namespace.

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


async def queues_post_authorization_rule(request: web.Request, resource_group_name, namespace_name, queue_name, authorization_rule_name, api_version, subscription_id) -> web.Response:
    """queues_post_authorization_rule

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
