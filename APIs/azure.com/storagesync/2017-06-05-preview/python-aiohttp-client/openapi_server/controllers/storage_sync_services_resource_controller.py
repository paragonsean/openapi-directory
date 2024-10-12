from typing import List, Dict
from aiohttp import web

from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.storage_sync_service import StorageSyncService
from openapi_server.models.storage_sync_service_array import StorageSyncServiceArray
from openapi_server import util


async def storage_sync_services_create(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, parameters) -> web.Response:
    """storage_sync_services_create

    Create a new StorageSyncService.

    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param parameters: Storage Sync Service resource name.
    :type parameters: dict | bytes

    """
    parameters = StorageSyncService.from_dict(parameters)
    return web.Response(status=200)


async def storage_sync_services_delete(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name) -> web.Response:
    """storage_sync_services_delete

    Delete a given StorageSyncService.

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


async def storage_sync_services_get(request: web.Request, subscription_id, resource_group_name, storage_sync_service_name, api_version) -> web.Response:
    """storage_sync_services_get

    Get a given StorageSyncService.

    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_sync_services_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """storage_sync_services_list_by_resource_group

    Get a StorageSyncService list by Resource group name.

    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_sync_services_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """storage_sync_services_list_by_subscription

    Get a StorageSyncService list by subscription.

    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_sync_services_update(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, parameters=None) -> web.Response:
    """storage_sync_services_update

    Patch a given StorageSyncService.

    :param subscription_id: Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param parameters: Storage Sync Service resource.
    :type parameters: dict | bytes

    """
    parameters = StorageSyncService.from_dict(parameters)
    return web.Response(status=200)
