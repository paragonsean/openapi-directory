from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_request import BackupRequest
from openapi_server.models.post_backup_response import PostBackupResponse
from openapi_server.models.post_restore_request import PostRestoreRequest
from openapi_server.models.pre_restore_request import PreRestoreRequest
from openapi_server.models.recall_action_parameters import RecallActionParameters
from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server import util


async def cloud_endpoints_post_backup_0(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_post_backup_0

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


async def cloud_endpoints_post_restore_0(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_post_restore_0

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


async def cloud_endpoints_pre_backup_0(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_pre_backup_0

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


async def cloud_endpoints_pre_restore_0(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name, parameters) -> web.Response:
    """cloud_endpoints_pre_restore_0

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


async def cloud_endpoints_restoreheartbeat_0(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, cloud_endpoint_name) -> web.Response:
    """cloud_endpoints_restoreheartbeat_0

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


async def server_endpoints_recall_action_0(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, server_endpoint_name, parameters) -> web.Response:
    """server_endpoints_recall_action_0

    Recall a server endpoint.

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
    :param server_endpoint_name: Name of Server Endpoint object.
    :type server_endpoint_name: str
    :param parameters: Body of Recall Action object.
    :type parameters: dict | bytes

    """
    parameters = RecallActionParameters.from_dict(parameters)
    return web.Response(status=200)


async def workflows_abort_0(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, workflow_id) -> web.Response:
    """workflows_abort_0

    Abort the given workflow.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param workflow_id: workflow Id
    :type workflow_id: str

    """
    return web.Response(status=200)
