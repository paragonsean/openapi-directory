from typing import List, Dict
from aiohttp import web

from openapi_server.models.drive import Drive
from openapi_server.models.drive_list import DriveList
from openapi_server import util


async def drives_get(request: web.Request, subscription_id, resource_group_name, location, scale_unit, storage_sub_system, drive, api_version) -> web.Response:
    """drives_get

    Return the requested a storage drive.

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
    :param drive: Name of the storage drive.
    :type drive: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def drives_list(request: web.Request, subscription_id, resource_group_name, location, scale_unit, storage_sub_system, api_version, filter=None) -> web.Response:
    """drives_list

    Returns a list of all storage drives at a location.

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
