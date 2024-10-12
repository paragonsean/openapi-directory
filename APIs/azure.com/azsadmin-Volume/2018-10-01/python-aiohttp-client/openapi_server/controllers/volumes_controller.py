from typing import List, Dict
from aiohttp import web

from openapi_server.models.volume import Volume
from openapi_server.models.volume_list import VolumeList
from openapi_server import util


async def volumes_get(request: web.Request, subscription_id, resource_group_name, location, scale_unit, storage_sub_system, volume, api_version) -> web.Response:
    """volumes_get

    Return the requested a storage volume.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param scale_unit: Name of the scale units.
    :type scale_unit: str
    :param storage_sub_system: Name of the storage system.
    :type storage_sub_system: str
    :param volume: Name of the storage volume.
    :type volume: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def volumes_list(request: web.Request, subscription_id, resource_group_name, location, scale_unit, storage_sub_system, api_version, filter=None) -> web.Response:
    """volumes_list

    Returns a list of all storage volumes at a location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param scale_unit: Name of the scale units.
    :type scale_unit: str
    :param storage_sub_system: Name of the storage system.
    :type storage_sub_system: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
