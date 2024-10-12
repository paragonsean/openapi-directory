from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_service import DeviceService
from openapi_server.models.device_service_description_list_result import DeviceServiceDescriptionListResult
from openapi_server.models.device_service_properties import DeviceServiceProperties
from openapi_server.models.error_details import ErrorDetails
from openapi_server import util


async def services_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, device_name, device_service, if_match=None) -> web.Response:
    """Create or update the metadata of a Windows IoT Device Service.

    Create or update the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the Windows IoT Device Service.
    :type resource_group_name: str
    :param device_name: The name of the Windows IoT Device Service.
    :type device_name: str
    :param device_service: The Windows IoT Device Service metadata and security metadata.
    :type device_service: dict | bytes
    :param if_match: ETag of the Windows IoT Device Service. Do not specify for creating a new Windows IoT Device Service. Required to update an existing Windows IoT Device Service.
    :type if_match: str

    """
    device_service = DeviceServiceProperties.from_dict(device_service)
    return web.Response(status=200)


async def services_delete(request: web.Request, api_version, subscription_id, resource_group_name, device_name) -> web.Response:
    """services_delete

    Delete a Windows IoT Device Service.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the Windows IoT Device Service.
    :type resource_group_name: str
    :param device_name: The name of the Windows IoT Device Service.
    :type device_name: str

    """
    return web.Response(status=200)


async def services_get(request: web.Request, api_version, subscription_id, resource_group_name, device_name) -> web.Response:
    """services_get

    Get the non-security related metadata of a Windows IoT Device Service.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the Windows IoT Device Service.
    :type resource_group_name: str
    :param device_name: The name of the Windows IoT Device Service.
    :type device_name: str

    """
    return web.Response(status=200)


async def services_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """services_list

    Get all the IoT hubs in a subscription.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def services_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """services_list_by_resource_group

    Get all the IoT hubs in a resource group.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the Windows IoT Device Service.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def services_update(request: web.Request, api_version, subscription_id, resource_group_name, device_name, device_service, if_match=None) -> web.Response:
    """Updates the metadata of a Windows IoT Device Service.

    Updates the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the Windows IoT Device Service.
    :type resource_group_name: str
    :param device_name: The name of the Windows IoT Device Service.
    :type device_name: str
    :param device_service: The Windows IoT Device Service metadata and security metadata.
    :type device_service: dict | bytes
    :param if_match: ETag of the Windows IoT Device Service. Do not specify for creating a brand new Windows IoT Device Service. Required to update an existing Windows IoT Device Service.
    :type if_match: str

    """
    device_service = DeviceServiceProperties.from_dict(device_service)
    return web.Response(status=200)
