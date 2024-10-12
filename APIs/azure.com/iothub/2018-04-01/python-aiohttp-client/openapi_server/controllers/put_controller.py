from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.event_hub_consumer_group_info import EventHubConsumerGroupInfo
from openapi_server.models.iot_hub_description import IotHubDescription
from openapi_server import util


async def iot_hub_resource_create_event_hub_consumer_group(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, event_hub_endpoint_name, name) -> web.Response:
    """Add a consumer group to an Event Hub-compatible endpoint in an IoT hub

    Add a consumer group to an Event Hub-compatible endpoint in an IoT hub.

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
    :param name: The name of the consumer group to add.
    :type name: str

    """
    return web.Response(status=200)


async def iot_hub_resource_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, iot_hub_description, if_match=None) -> web.Response:
    """Create or update the metadata of an IoT hub.

    Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoT hub.
    :type resource_group_name: str
    :param resource_name: The name of the IoT hub.
    :type resource_name: str
    :param iot_hub_description: The IoT hub metadata and security metadata.
    :type iot_hub_description: dict | bytes
    :param if_match: ETag of the IoT Hub. Do not specify for creating a brand new IoT Hub. Required to update an existing IoT Hub.
    :type if_match: str

    """
    iot_hub_description = IotHubDescription.from_dict(iot_hub_description)
    return web.Response(status=200)
