from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.iot_hub_description import IotHubDescription
from openapi_server import util


async def iot_hub_resource_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Delete an IoT hub

    Delete an IoT hub.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_delete_event_hub_consumer_group(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, event_hub_endpoint_name, name) -> web.Response:
    """Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub

    Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param event_hub_endpoint_name: The name of the Event Hub-compatible endpoint in the IoT hub.
    :type event_hub_endpoint_name: str
    :param name: The name of the consumer group to delete.
    :type name: str

    """
    return web.Response(status=200)
