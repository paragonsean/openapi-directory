from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_subscription import EventSubscription
from openapi_server.models.event_subscription_full_url import EventSubscriptionFullUrl
from openapi_server.models.event_subscription_update_parameters import EventSubscriptionUpdateParameters
from openapi_server.models.event_subscriptions_list_result import EventSubscriptionsListResult
from openapi_server import util


async def event_subscriptions_create(request: web.Request, scope, event_subscription_name, api_version, event_subscription_info) -> web.Response:
    """Create an event subscription

    Asynchronously creates a new event subscription to the specified scope. Existing event subscriptions cannot be updated with this API and should instead use the Update event subscription API.

    :param scope: The scope of the resource to which the event subscription needs to be created. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription to be created. Event subscription names must be between 3 and 64 characters in length and use alphanumeric letters only.
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param event_subscription_info: Event subscription properties containing the destination and filter information
    :type event_subscription_info: dict | bytes

    """
    event_subscription_info = EventSubscription.from_dict(event_subscription_info)
    return web.Response(status=200)


async def event_subscriptions_delete(request: web.Request, scope, event_subscription_name, api_version) -> web.Response:
    """Delete an event subscription

    Delete an existing event subscription

    :param scope: The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_get(request: web.Request, scope, event_subscription_name, api_version) -> web.Response:
    """Get an event subscription

    Get properties of an event subscription

    :param scope: The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_get_full_url(request: web.Request, scope, event_subscription_name, api_version) -> web.Response:
    """Get full URL of an event subscription

    Get the full endpoint URL for an event subscription

    :param scope: The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_by_resource(request: web.Request, subscription_id, resource_group_name, provider_namespace, resource_type_name, resource_name, api_version) -> web.Response:
    """List all event subscriptions for a specific topic

    List all event subscriptions that have been created for a specific topic

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param provider_namespace: Namespace of the provider of the topic
    :type provider_namespace: str
    :param resource_type_name: Name of the resource type
    :type resource_type_name: str
    :param resource_name: Name of the resource
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_global_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """List all global event subscriptions under an Azure subscription and resource group

    List all global event subscriptions under a specific Azure subscription and resource group

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_global_by_resource_group_for_topic_type(request: web.Request, subscription_id, resource_group_name, topic_type_name, api_version) -> web.Response:
    """List all global event subscriptions under a resource group for a topic type

    List all global event subscriptions under a resource group for a specific topic type.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param topic_type_name: Name of the topic type
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_global_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get an aggregated list of all global event subscriptions under an Azure subscription

    List all aggregated global event subscriptions under a specific Azure subscription

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_global_by_subscription_for_topic_type(request: web.Request, subscription_id, topic_type_name, api_version) -> web.Response:
    """List all global event subscriptions for a topic type

    List all global event subscriptions under an Azure subscription for a topic type.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param topic_type_name: Name of the topic type
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_regional_by_resource_group(request: web.Request, subscription_id, resource_group_name, location, api_version) -> web.Response:
    """List all regional event subscriptions under an Azure subscription and resource group

    List all event subscriptions from the given location under a specific Azure subscription and resource group

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param location: Name of the location
    :type location: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_regional_by_resource_group_for_topic_type(request: web.Request, subscription_id, resource_group_name, location, topic_type_name, api_version) -> web.Response:
    """List all regional event subscriptions under an Azure subscription and resource group for a topic type

    List all event subscriptions from the given location under a specific Azure subscription and resource group and topic type

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param location: Name of the location
    :type location: str
    :param topic_type_name: Name of the topic type
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_regional_by_subscription(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """List all regional event subscriptions under an Azure subscription

    List all event subscriptions from the given location under a specific Azure subscription

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Name of the location
    :type location: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_regional_by_subscription_for_topic_type(request: web.Request, subscription_id, location, topic_type_name, api_version) -> web.Response:
    """List all regional event subscriptions under an Azure subscription for a topic type

    List all event subscriptions from the given location under a specific Azure subscription and topic type.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Name of the location
    :type location: str
    :param topic_type_name: Name of the topic type
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_update(request: web.Request, scope, event_subscription_name, api_version, event_subscription_update_parameters) -> web.Response:
    """Update an event subscription

    Asynchronously updates an existing event subscription.

    :param scope: The scope of existing event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription to be created
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param event_subscription_update_parameters: Updated event subscription information
    :type event_subscription_update_parameters: dict | bytes

    """
    event_subscription_update_parameters = EventSubscriptionUpdateParameters.from_dict(event_subscription_update_parameters)
    return web.Response(status=200)
