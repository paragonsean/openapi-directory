from typing import List, Dict
from aiohttp import web

from openapi_server.models.digital_twins_integration_resource_list_result import DigitalTwinsIntegrationResourceListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.integration_resource import IntegrationResource
from openapi_server import util


async def digital_twins_io_t_hubs_list(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """digital_twins_io_t_hubs_list

    Get DigitalTwinsInstance IoTHubs.

    :param api_version: Version of the DigitalTwinsInstance Management API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :type resource_group_name: str
    :param resource_name: The name of the DigitalTwinsInstance.
    :type resource_name: str

    """
    return web.Response(status=200)


async def io_t_hub_create_or_update(request: web.Request, scope, integration_resource_name, iot_hub_description) -> web.Response:
    """io_t_hub_create_or_update

    Creates or Updates an IoTHub Integration with DigitalTwinsInstances.

    :param scope: The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}.
    :type scope: str
    :param integration_resource_name: Name of IoTHub and DigitalTwinsInstance integration instance.
    :type integration_resource_name: str
    :param iot_hub_description: The IoTHub metadata.
    :type iot_hub_description: dict | bytes

    """
    iot_hub_description = IntegrationResource.from_dict(iot_hub_description)
    return web.Response(status=200)


async def io_t_hub_delete(request: web.Request, scope, integration_resource_name) -> web.Response:
    """io_t_hub_delete

    Deletes a DigitalTwinsInstance link with IoTHub.

    :param scope: The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}.
    :type scope: str
    :param integration_resource_name: Name of IoTHub and DigitalTwinsInstance integration instance.
    :type integration_resource_name: str

    """
    return web.Response(status=200)


async def io_t_hub_get(request: web.Request, scope, integration_resource_name) -> web.Response:
    """io_t_hub_get

    Gets properties of an IoTHub Integration.

    :param scope: The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}.
    :type scope: str
    :param integration_resource_name: Name of IoTHub and DigitalTwinsInstance integration instance.
    :type integration_resource_name: str

    """
    return web.Response(status=200)
