from typing import List, Dict
from aiohttp import web

from openapi_server.models.digital_twins_description import DigitalTwinsDescription
from openapi_server.models.digital_twins_description_list_result import DigitalTwinsDescriptionListResult
from openapi_server.models.digital_twins_patch_description import DigitalTwinsPatchDescription
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def digital_twins_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, digital_twins_create) -> web.Response:
    """digital_twins_create_or_update

    Create or update the metadata of a DigitalTwinsInstance. The usual pattern to modify a property is to retrieve the DigitalTwinsInstance and security metadata, and then combine them with the modified values in a new body to update the DigitalTwinsInstance.

    :param api_version: Version of the DigitalTwinsInstance Management API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :type resource_group_name: str
    :param resource_name: The name of the DigitalTwinsInstance.
    :type resource_name: str
    :param digital_twins_create: The DigitalTwinsInstance and security metadata.
    :type digital_twins_create: dict | bytes

    """
    digital_twins_create = DigitalTwinsDescription.from_dict(digital_twins_create)
    return web.Response(status=200)


async def digital_twins_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """digital_twins_delete

    Delete a DigitalTwinsInstance.

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


async def digital_twins_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """digital_twins_get

    Get DigitalTwinsInstances resource.

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


async def digital_twins_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """digital_twins_list

    Get all the DigitalTwinsInstances in a subscription.

    :param api_version: Version of the DigitalTwinsInstance Management API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str

    """
    return web.Response(status=200)


async def digital_twins_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """digital_twins_list_by_resource_group

    Get all the DigitalTwinsInstances in a resource group.

    :param api_version: Version of the DigitalTwinsInstance Management API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def digital_twins_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, digital_twins_patch_description) -> web.Response:
    """digital_twins_update

    Update metadata of DigitalTwinsInstance.

    :param api_version: Version of the DigitalTwinsInstance Management API.
    :type api_version: str
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :type resource_group_name: str
    :param resource_name: The name of the DigitalTwinsInstance.
    :type resource_name: str
    :param digital_twins_patch_description: The DigitalTwinsInstance and security metadata.
    :type digital_twins_patch_description: dict | bytes

    """
    digital_twins_patch_description = DigitalTwinsPatchDescription.from_dict(digital_twins_patch_description)
    return web.Response(status=200)
