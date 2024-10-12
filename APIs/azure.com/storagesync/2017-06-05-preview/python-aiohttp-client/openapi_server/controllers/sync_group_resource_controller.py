from typing import List, Dict
from aiohttp import web

from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.sync_group import SyncGroup
from openapi_server.models.sync_group_array import SyncGroupArray
from openapi_server import util


async def sync_groups_create(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, parameters) -> web.Response:
    """sync_groups_create

    Create a new SyncGroup.

    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param parameters: Sync Group Body
    :type parameters: dict | bytes

    """
    parameters = SyncGroup.from_dict(parameters)
    return web.Response(status=200)


async def sync_groups_delete(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name) -> web.Response:
    """sync_groups_delete

    Delete a given SyncGroup.

    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str

    """
    return web.Response(status=200)


async def sync_groups_get(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name) -> web.Response:
    """sync_groups_get

    Get a given SyncGroup.

    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str

    """
    return web.Response(status=200)


async def sync_groups_list_by_storage_sync_service(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name) -> web.Response:
    """sync_groups_list_by_storage_sync_service

    Get a SyncGroup List.

    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str

    """
    return web.Response(status=200)
