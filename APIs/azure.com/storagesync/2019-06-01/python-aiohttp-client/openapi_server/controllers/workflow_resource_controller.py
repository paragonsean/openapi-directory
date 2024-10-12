from typing import List, Dict
from aiohttp import web

from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.workflow import Workflow
from openapi_server.models.workflow_array import WorkflowArray
from openapi_server import util


async def workflows_abort(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, workflow_id) -> web.Response:
    """workflows_abort

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


async def workflows_get(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, workflow_id) -> web.Response:
    """workflows_get

    Get Workflows resource

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


async def workflows_list_by_storage_sync_service(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name) -> web.Response:
    """workflows_list_by_storage_sync_service

    Get a Workflow List

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str

    """
    return web.Response(status=200)
