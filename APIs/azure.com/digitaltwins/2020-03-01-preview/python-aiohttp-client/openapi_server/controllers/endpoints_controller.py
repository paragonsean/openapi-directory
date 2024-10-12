from typing import List, Dict
from aiohttp import web

from openapi_server.models.digital_twins_endpoint_resource import DigitalTwinsEndpointResource
from openapi_server.models.digital_twins_endpoint_resource_list_result import DigitalTwinsEndpointResourceListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def digital_twins_endpoint_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, endpoint_name, endpoint_description) -> web.Response:
    """digital_twins_endpoint_create_or_update

    Create or update DigitalTwinsInstance endpoint.

    :param api_version: Version of the DigitalTwinsInstance Management API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :type resource_group_name: str
    :param resource_name: The name of the DigitalTwinsInstance.
    :type resource_name: str
    :param endpoint_name: Name of Endpoint Resource.
    :type endpoint_name: str
    :param endpoint_description: The DigitalTwinsInstance endpoint metadata and security metadata.
    :type endpoint_description: dict | bytes

    """
    endpoint_description = DigitalTwinsEndpointResource.from_dict(endpoint_description)
    return web.Response(status=200)


async def digital_twins_endpoint_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, endpoint_name) -> web.Response:
    """digital_twins_endpoint_delete

    Delete a DigitalTwinsInstance endpoint.

    :param api_version: Version of the DigitalTwinsInstance Management API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :type resource_group_name: str
    :param resource_name: The name of the DigitalTwinsInstance.
    :type resource_name: str
    :param endpoint_name: Name of Endpoint Resource.
    :type endpoint_name: str

    """
    return web.Response(status=200)


async def digital_twins_endpoint_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, endpoint_name) -> web.Response:
    """digital_twins_endpoint_get

    Get DigitalTwinsInstances Endpoint.

    :param api_version: Version of the DigitalTwinsInstance Management API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :type resource_group_name: str
    :param resource_name: The name of the DigitalTwinsInstance.
    :type resource_name: str
    :param endpoint_name: Name of Endpoint Resource.
    :type endpoint_name: str

    """
    return web.Response(status=200)


async def digital_twins_endpoint_list(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """digital_twins_endpoint_list

    Get DigitalTwinsInstance Endpoints.

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
