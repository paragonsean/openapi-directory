from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.volume_resource_description import VolumeResourceDescription
from openapi_server.models.volume_resource_description_list import VolumeResourceDescriptionList
from openapi_server import util


async def volume_create(request: web.Request, subscription_id, api_version, resource_group_name, volume_resource_name, volume_resource_description) -> web.Response:
    """Creates or updates a volume resource.

    Creates a volume resource with the specified name, description and properties. If a volume resource with the same name exists, then it is updated with the specified description and properties.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param volume_resource_name: The identity of the volume.
    :type volume_resource_name: str
    :param volume_resource_description: Description for creating a Volume resource.
    :type volume_resource_description: dict | bytes

    """
    volume_resource_description = VolumeResourceDescription.from_dict(volume_resource_description)
    return web.Response(status=200)


async def volume_delete(request: web.Request, subscription_id, api_version, resource_group_name, volume_resource_name) -> web.Response:
    """Deletes the volume resource.

    Deletes the volume resource identified by the name.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param volume_resource_name: The identity of the volume.
    :type volume_resource_name: str

    """
    return web.Response(status=200)


async def volume_get(request: web.Request, subscription_id, api_version, resource_group_name, volume_resource_name) -> web.Response:
    """Gets the volume resource with the given name.

    Gets the information about the volume resource with the given name. The information include the description and other properties of the volume.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param volume_resource_name: The identity of the volume.
    :type volume_resource_name: str

    """
    return web.Response(status=200)


async def volume_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """Gets all the volume resources in a given resource group.

    Gets the information about all volume resources in a given resource group. The information include the description and other properties of the Volume.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def volume_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all the volume resources in a given subscription.

    Gets the information about all volume resources in a given resource group. The information include the description and other properties of the volume.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str

    """
    return web.Response(status=200)
