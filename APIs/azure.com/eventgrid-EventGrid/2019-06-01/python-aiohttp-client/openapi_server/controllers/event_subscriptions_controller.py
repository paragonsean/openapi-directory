from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_subscription import EventSubscription
from openapi_server.models.event_subscription_full_url import EventSubscriptionFullUrl
from openapi_server.models.event_subscription_update_parameters import EventSubscriptionUpdateParameters
from openapi_server.models.event_subscriptions_list_result import EventSubscriptionsListResult
from openapi_server import util


async def event_subscriptions_create_or_update(request: web.Request, scope, event_subscription_name, api_version, event_subscription_info) -> web.Response:
    """Create or update an event subscription.

    Asynchronously creates a new event subscription or updates an existing event subscription based on the specified scope.

    :param scope: The identifier of the resource to which the event subscription needs to be created or updated. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription. Event subscription names must be between 3 and 64 characters in length and should use alphanumeric letters only.
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param event_subscription_info: Event subscription properties containing the destination and filter information.
    :type event_subscription_info: dict | bytes

    """
    event_subscription_info = EventSubscription.from_dict(event_subscription_info)
    return web.Response(status=200)


async def event_subscriptions_delete(request: web.Request, scope, event_subscription_name, api_version) -> web.Response:
    """Delete an event subscription.

    Delete an existing event subscription.

    :param scope: The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription.
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_get(request: web.Request, scope, event_subscription_name, api_version) -> web.Response:
    """Get an event subscription.

    Get properties of an event subscription.

    :param scope: The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription.
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_get_full_url(request: web.Request, scope, event_subscription_name, api_version) -> web.Response:
    """Get full URL of an event subscription.

    Get the full endpoint URL for an event subscription.

    :param scope: The scope of the event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription.
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def event_subscriptions_list_by_domain_topic(request: web.Request, subscription_id, resource_group_name, domain_name, topic_name, api_version, filter=None, top=None) -> web.Response:
    """List all event subscriptions for a specific domain topic.

    List all event subscriptions that have been created for a specific domain topic.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param domain_name: Name of the top level domain.
    :type domain_name: str
    :param topic_name: Name of the domain topic.
    :type topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_list_by_resource(request: web.Request, subscription_id, resource_group_name, provider_namespace, resource_type_name, resource_name, api_version, filter=None, top=None) -> web.Response:
    """List all event subscriptions for a specific topic.

    List all event subscriptions that have been created for a specific topic.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param provider_namespace: Namespace of the provider of the topic.
    :type provider_namespace: str
    :param resource_type_name: Name of the resource type.
    :type resource_type_name: str
    :param resource_name: Name of the resource.
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_list_global_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, filter=None, top=None) -> web.Response:
    """List all global event subscriptions under an Azure subscription and resource group.

    List all global event subscriptions under a specific Azure subscription and resource group.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_list_global_by_resource_group_for_topic_type(request: web.Request, subscription_id, resource_group_name, topic_type_name, api_version, filter=None, top=None) -> web.Response:
    """List all global event subscriptions under a resource group for a topic type.

    List all global event subscriptions under a resource group for a specific topic type.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param topic_type_name: Name of the topic type.
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_list_global_by_subscription(request: web.Request, subscription_id, api_version, filter=None, top=None) -> web.Response:
    """Get an aggregated list of all global event subscriptions under an Azure subscription.

    List all aggregated global event subscriptions under a specific Azure subscription.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_list_global_by_subscription_for_topic_type(request: web.Request, subscription_id, topic_type_name, api_version, filter=None, top=None) -> web.Response:
    """List all global event subscriptions for a topic type.

    List all global event subscriptions under an Azure subscription for a topic type.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param topic_type_name: Name of the topic type.
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_list_regional_by_resource_group(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None, top=None) -> web.Response:
    """List all regional event subscriptions under an Azure subscription and resource group.

    List all event subscriptions from the given location under a specific Azure subscription and resource group.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param location: Name of the location.
    :type location: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_list_regional_by_resource_group_for_topic_type(request: web.Request, subscription_id, resource_group_name, location, topic_type_name, api_version, filter=None, top=None) -> web.Response:
    """List all regional event subscriptions under an Azure subscription and resource group for a topic type.

    List all event subscriptions from the given location under a specific Azure subscription and resource group and topic type.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param location: Name of the location.
    :type location: str
    :param topic_type_name: Name of the topic type.
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_list_regional_by_subscription(request: web.Request, subscription_id, location, api_version, filter=None, top=None) -> web.Response:
    """List all regional event subscriptions under an Azure subscription.

    List all event subscriptions from the given location under a specific Azure subscription.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Name of the location.
    :type location: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_list_regional_by_subscription_for_topic_type(request: web.Request, subscription_id, location, topic_type_name, api_version, filter=None, top=None) -> web.Response:
    """List all regional event subscriptions under an Azure subscription for a topic type.

    List all event subscriptions from the given location under a specific Azure subscription and topic type.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Name of the location.
    :type location: str
    :param topic_type_name: Name of the topic type.
    :type topic_type_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;.
    :type filter: str
    :param top: The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    :type top: int

    """
    return web.Response(status=200)


async def event_subscriptions_update(request: web.Request, scope, event_subscription_name, api_version, event_subscription_update_parameters) -> web.Response:
    """Update an event subscription.

    Asynchronously updates an existing event subscription.

    :param scope: The scope of existing event subscription. The scope can be a subscription, or a resource group, or a top level resource belonging to a resource provider namespace, or an EventGrid topic. For example, use &#39;/subscriptions/{subscriptionId}/&#39; for a subscription, &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}&#39; for a resource group, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}&#39; for a resource, and &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/topics/{topicName}&#39; for an EventGrid topic.
    :type scope: str
    :param event_subscription_name: Name of the event subscription to be updated.
    :type event_subscription_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param event_subscription_update_parameters: Updated event subscription information.
    :type event_subscription_update_parameters: dict | bytes

    """
    event_subscription_update_parameters = EventSubscriptionUpdateParameters.from_dict(event_subscription_update_parameters)
    return web.Response(status=200)
