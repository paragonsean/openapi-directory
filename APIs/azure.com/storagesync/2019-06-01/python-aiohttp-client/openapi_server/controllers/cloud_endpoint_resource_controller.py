from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_request import BackupRequest
from openapi_server.models.cloud_endpoint import CloudEndpoint
from openapi_server.models.cloud_endpoint_array import CloudEndpointArray
from openapi_server.models.cloud_endpoint_create_parameters import CloudEndpointCreateParameters
from openapi_server.models.post_backup_response import PostBackupResponse
from openapi_server.models.post_restore_request import PostRestoreRequest
from openapi_server.models.pre_restore_request import PreRestoreRequest
from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.trigger_change_detection_parameters import TriggerChangeDetectionParameters
from openapi_server import util


async def cloud_endpoints_create(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_create

    Create a new CloudEndpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str
    :param parameters: Body of Cloud Endpoint resource.
    :type parameters: dict | bytes

    """
    parameters = CloudEndpointCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def cloud_endpoints_delete(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name) -> web.Response:
    """cloud_endpoints_delete

    Delete a given CloudEndpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str

    """
    return web.Response(status=200)


async def cloud_endpoints_get(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name) -> web.Response:
    """cloud_endpoints_get

    Get a given CloudEndpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str

    """
    return web.Response(status=200)


async def cloud_endpoints_list_by_sync_group(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name) -> web.Response:
    """cloud_endpoints_list_by_sync_group

    Get a CloudEndpoint List.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str

    """
    return web.Response(status=200)


async def cloud_endpoints_post_backup(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_post_backup

    Post Backup a given CloudEndpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str
    :param parameters: Body of Backup request.
    :type parameters: dict | bytes

    """
    parameters = BackupRequest.from_dict(parameters)
    return web.Response(status=200)


async def cloud_endpoints_post_restore(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_post_restore

    Post Restore a given CloudEndpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str
    :param parameters: Body of Cloud Endpoint object.
    :type parameters: dict | bytes

    """
    parameters = PostRestoreRequest.from_dict(parameters)
    return web.Response(status=200)


async def cloud_endpoints_pre_backup(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_pre_backup

    Pre Backup a given CloudEndpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str
    :param parameters: Body of Backup request.
    :type parameters: dict | bytes

    """
    parameters = BackupRequest.from_dict(parameters)
    return web.Response(status=200)


async def cloud_endpoints_pre_restore(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_pre_restore

    Pre Restore a given CloudEndpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str
    :param parameters: Body of Cloud Endpoint object.
    :type parameters: dict | bytes

    """
    parameters = PreRestoreRequest.from_dict(parameters)
    return web.Response(status=200)


async def cloud_endpoints_restoreheartbeat(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name) -> web.Response:
    """cloud_endpoints_restoreheartbeat

    Restore Heartbeat a given CloudEndpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str

    """
    return web.Response(status=200)


async def cloud_endpoints_trigger_change_detection(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_trigger_change_detection

    Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param sync_group_name: Name of Sync Group resource.
    :type sync_group_name: str
    :param cloud_endpoint_name: Name of Cloud Endpoint object.
    :type cloud_endpoint_name: str
    :param parameters: Trigger Change Detection Action parameters.
    :type parameters: dict | bytes

    """
    parameters = TriggerChangeDetectionParameters.from_dict(parameters)
    return web.Response(status=200)
