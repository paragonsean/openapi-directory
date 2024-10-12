from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.volume_resource_description import VolumeResourceDescription
from openapi_server.models.volume_resource_description_list import VolumeResourceDescriptionList
from openapi_server import util


async def volume_create(request: web.Request, subscription_id, api_version, resource_group_name, volume_name, volume_resource_description) -> web.Response:
    """Creates or updates a volume resource.

    Creates a volume resource with the specified name and description. If a volume with the same name already exists, then its description is updated to the one indicated in this request. 

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param volume_name: The identity of the volume.
    :type volume_name: str
    :param volume_resource_description: Description for creating a volume resource.
    :type volume_resource_description: dict | bytes

    """
    volume_resource_description = VolumeResourceDescription.from_dict(volume_resource_description)
    return web.Response(status=200)


async def volume_delete(request: web.Request, subscription_id, api_version, resource_group_name, volume_name) -> web.Response:
    """Deletes the volume resource.

    Deletes the volume identified by the name.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param volume_name: The identity of the volume.
    :type volume_name: str

    """
    return web.Response(status=200)


async def volume_get(request: web.Request, subscription_id, api_version, resource_group_name, volume_name) -> web.Response:
    """Gets the volume resource.

    Gets the information about the volume resource with a given name. This information includes the volume description and other runtime information. 

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param volume_name: The identity of the volume.
    :type volume_name: str

    """
    return web.Response(status=200)


async def volume_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """Gets all the volume resources in a given resource group.

    Gets the information about all volume resources in a given resource group. The information includes the volume description and other runtime information. 

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def volume_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all the volume resources in a given subscription.

    Gets the information about all volume resources in a given subscription. The information includes the volume description and other runtime information. 

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str

    """
    return web.Response(status=200)
