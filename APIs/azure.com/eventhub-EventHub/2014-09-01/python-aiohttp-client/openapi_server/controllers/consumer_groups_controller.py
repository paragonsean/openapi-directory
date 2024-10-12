from typing import List, Dict
from aiohttp import web

from openapi_server.models.consumer_group_create_or_update_parameters import ConsumerGroupCreateOrUpdateParameters
from openapi_server.models.consumer_group_list_result import ConsumerGroupListResult
from openapi_server.models.consumer_group_resource import ConsumerGroupResource
from openapi_server import util


async def consumer_groups_create_or_update(request: web.Request, resource_group_name, namespace_name, event_hub_name, consumer_group_name, api_version, subscription_id, parameters) -> web.Response:
    """consumer_groups_create_or_update

    Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param consumer_group_name: The consumer group name
    :type consumer_group_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create or update a consumer group resource.
    :type parameters: dict | bytes

    """
    parameters = ConsumerGroupCreateOrUpdateParameters.from_dict(parameters)
    return web.Response(status=200)


async def consumer_groups_delete(request: web.Request, resource_group_name, namespace_name, event_hub_name, consumer_group_name, api_version, subscription_id) -> web.Response:
    """consumer_groups_delete

    Deletes a consumer group from the specified Event Hub and resource group.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param consumer_group_name: The consumer group name
    :type consumer_group_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def consumer_groups_get(request: web.Request, resource_group_name, namespace_name, event_hub_name, consumer_group_name, api_version, subscription_id) -> web.Response:
    """consumer_groups_get

    Gets a description for the specified consumer group.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param consumer_group_name: The consumer group name
    :type consumer_group_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def consumer_groups_list_all(request: web.Request, resource_group_name, namespace_name, event_hub_name, api_version, subscription_id) -> web.Response:
    """consumer_groups_list_all

    Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group exists in the Namespace.

    :param resource_group_name: Name of the resource group within the azure subscription.
    :type resource_group_name: str
    :param namespace_name: The Namespace name
    :type namespace_name: str
    :param event_hub_name: The Event Hub name
    :type event_hub_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
