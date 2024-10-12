from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_volume_resource_description_list import PagedVolumeResourceDescriptionList
from openapi_server.models.volume_resource_description import VolumeResourceDescription
from openapi_server import util


async def mesh_volume_create_or_update(request: web.Request, api_version, volume_resource_name, volume_resource_description) -> web.Response:
    """Creates or updates a Volume resource.

    Creates a Volume resource with the specified name, description and properties. If Volume resource with the same name exists, then it is updated with the specified description and properties.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param volume_resource_name: The identity of the volume.
    :type volume_resource_name: str
    :param volume_resource_description: Description for creating a Volume resource.
    :type volume_resource_description: dict | bytes

    """
    volume_resource_description = VolumeResourceDescription.from_dict(volume_resource_description)
    return web.Response(status=200)


async def mesh_volume_delete(request: web.Request, api_version, volume_resource_name) -> web.Response:
    """Deletes the Volume resource.

    Deletes the Volume resource identified by the name.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param volume_resource_name: The identity of the volume.
    :type volume_resource_name: str

    """
    return web.Response(status=200)


async def mesh_volume_get(request: web.Request, api_version, volume_resource_name) -> web.Response:
    """Gets the Volume resource with the given name.

    Gets the information about the Volume resource with the given name. The information include the description and other properties of the Volume.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param volume_resource_name: The identity of the volume.
    :type volume_resource_name: str

    """
    return web.Response(status=200)


async def mesh_volume_list(request: web.Request, api_version) -> web.Response:
    """Lists all the volume resources.

    Gets the information about all volume resources in a given resource group. The information include the description and other properties of the Volume.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str

    """
    return web.Response(status=200)
