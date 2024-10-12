from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.io_t_spaces_description import IoTSpacesDescription
from openapi_server.models.io_t_spaces_patch_description import IoTSpacesPatchDescription
from openapi_server import util


async def io_t_spaces_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, iot_space_description) -> web.Response:
    """io_t_spaces_create_or_update

    Create or update the metadata of an IoTSpaces instance. The usual pattern to modify a property is to retrieve the IoTSpaces instance metadata and security metadata, and then combine them with the modified values in a new body to update the IoTSpaces instance.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoTSpaces instance.
    :type resource_group_name: str
    :param resource_name: The name of the IoTSpaces instance.
    :type resource_name: str
    :param iot_space_description: The IoTSpaces instance metadata and security metadata.
    :type iot_space_description: dict | bytes

    """
    iot_space_description = IoTSpacesDescription.from_dict(iot_space_description)
    return web.Response(status=200)


async def io_t_spaces_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """io_t_spaces_delete

    Delete an IoTSpaces instance.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoTSpaces instance.
    :type resource_group_name: str
    :param resource_name: The name of the IoTSpaces instance.
    :type resource_name: str

    """
    return web.Response(status=200)


async def io_t_spaces_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """io_t_spaces_get

    Get the metadata of a IoTSpaces instance.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoTSpaces instance.
    :type resource_group_name: str
    :param resource_name: The name of the IoTSpaces instance.
    :type resource_name: str

    """
    return web.Response(status=200)


async def io_t_spaces_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, iot_space_patch_description) -> web.Response:
    """io_t_spaces_update

    Update the metadata of a IoTSpaces instance.

    :param api_version: The version of the API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the IoTSpaces instance.
    :type resource_group_name: str
    :param resource_name: The name of the IoTSpaces instance.
    :type resource_name: str
    :param iot_space_patch_description: The IoTSpaces instance metadata and security metadata.
    :type iot_space_patch_description: dict | bytes

    """
    iot_space_patch_description = IoTSpacesPatchDescription.from_dict(iot_space_patch_description)
    return web.Response(status=200)
