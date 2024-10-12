from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_types_list_result import EventTypesListResult
from openapi_server.models.topic import Topic
from openapi_server.models.topic_regenerate_key_request import TopicRegenerateKeyRequest
from openapi_server.models.topic_shared_access_keys import TopicSharedAccessKeys
from openapi_server.models.topic_update_parameters import TopicUpdateParameters
from openapi_server.models.topics_list_result import TopicsListResult
from openapi_server import util


async def topics_create_or_update(request: web.Request, subscription_id, resource_group_name, topic_name, api_version, topic_info) -> web.Response:
    """Create a topic

    Asynchronously creates a new topic with the specified parameters.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param topic_name: Name of the topic
    :type topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param topic_info: Topic information
    :type topic_info: dict | bytes

    """
    topic_info = Topic.from_dict(topic_info)
    return web.Response(status=200)


async def topics_delete(request: web.Request, subscription_id, resource_group_name, topic_name, api_version) -> web.Response:
    """Delete a topic

    Delete existing topic

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param topic_name: Name of the topic
    :type topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def topics_get(request: web.Request, subscription_id, resource_group_name, topic_name, api_version) -> web.Response:
    """Get a topic

    Get properties of a topic

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param topic_name: Name of the topic
    :type topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def topics_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """List topics under a resource group

    List all the topics under a resource group

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def topics_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """List topics under an Azure subscription

    List all the topics under an Azure subscription

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def topics_list_event_types(request: web.Request, subscription_id, resource_group_name, provider_namespace, resource_type_name, resource_name, api_version) -> web.Response:
    """List topic event types

    List event types for a topic

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param provider_namespace: Namespace of the provider of the topic
    :type provider_namespace: str
    :param resource_type_name: Name of the topic type
    :type resource_type_name: str
    :param resource_name: Name of the topic
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def topics_list_shared_access_keys(request: web.Request, subscription_id, resource_group_name, topic_name, api_version) -> web.Response:
    """List keys for a topic

    List the two keys used to publish to a topic

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param topic_name: Name of the topic
    :type topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def topics_regenerate_key(request: web.Request, subscription_id, resource_group_name, topic_name, api_version, regenerate_key_request) -> web.Response:
    """Regenerate key for a topic

    Regenerate a shared access key for a topic

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param topic_name: Name of the topic
    :type topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param regenerate_key_request: Request body to regenerate key
    :type regenerate_key_request: dict | bytes

    """
    regenerate_key_request = TopicRegenerateKeyRequest.from_dict(regenerate_key_request)
    return web.Response(status=200)


async def topics_update(request: web.Request, subscription_id, resource_group_name, topic_name, api_version, topic_update_parameters) -> web.Response:
    """Update a topic

    Asynchronously updates a topic with the specified parameters.

    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param topic_name: Name of the topic
    :type topic_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param topic_update_parameters: Topic update information
    :type topic_update_parameters: dict | bytes

    """
    topic_update_parameters = TopicUpdateParameters.from_dict(topic_update_parameters)
    return web.Response(status=200)
