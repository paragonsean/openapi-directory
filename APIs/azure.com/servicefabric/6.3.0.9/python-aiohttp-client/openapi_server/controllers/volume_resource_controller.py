from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.volume_resource_description import VolumeResourceDescription
from openapi_server import util


async def create_volume_resource(request: web.Request, api_version, volume_resource_name, volume_resource_description) -> web.Response:
    """Creates or updates a volume resource.

    Creates a volume resource with the specified name and description. If a volume with the same name already exists, then its description is updated to the one indicated in this request.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param volume_resource_name: Service Fabric volume resource name.
    :type volume_resource_name: str
    :param volume_resource_description: Description for creating a volume resource.
    :type volume_resource_description: dict | bytes

    """
    volume_resource_description = VolumeResourceDescription.from_dict(volume_resource_description)
    return web.Response(status=200)


async def delete_volume_resource(request: web.Request, api_version, volume_resource_name) -> web.Response:
    """Deletes the volume resource.

    Deletes the volume identified by the name.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param volume_resource_name: Service Fabric volume resource name.
    :type volume_resource_name: str

    """
    return web.Response(status=200)


async def get_volume_resource(request: web.Request, api_version, volume_resource_name) -> web.Response:
    """Gets the volume resource.

    Gets the information about the volume resource with a given name. This information includes the volume description and other runtime information.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;.
    :type api_version: str
    :param volume_resource_name: Service Fabric volume resource name.
    :type volume_resource_name: str

    """
    return web.Response(status=200)
