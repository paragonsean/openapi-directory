from typing import List, Dict
from aiohttp import web

from openapi_server.models.registered_server import RegisteredServer
from openapi_server.models.registered_server_array import RegisteredServerArray
from openapi_server.models.registered_server_create_parameters import RegisteredServerCreateParameters
from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server.models.trigger_rollover_request import TriggerRolloverRequest
from openapi_server import util


async def registered_servers_create(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, server_id, parameters) -> web.Response:
    """registered_servers_create

    Add a new registered server.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param server_id: GUID identifying the on-premises server.
    :type server_id: str
    :param parameters: Body of Registered Server object.
    :type parameters: dict | bytes

    """
    parameters = RegisteredServerCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def registered_servers_delete(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, server_id) -> web.Response:
    """registered_servers_delete

    Delete the given registered server.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param server_id: GUID identifying the on-premises server.
    :type server_id: str

    """
    return web.Response(status=200)


async def registered_servers_get(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, server_id) -> web.Response:
    """registered_servers_get

    Get a given registered server.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param server_id: GUID identifying the on-premises server.
    :type server_id: str

    """
    return web.Response(status=200)


async def registered_servers_list_by_storage_sync_service(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name) -> web.Response:
    """registered_servers_list_by_storage_sync_service

    Get a given registered server list.

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


async def registered_servers_trigger_rollover(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, server_id, parameters) -> web.Response:
    """registered_servers_trigger_rollover

    Triggers Server certificate rollover.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param storage_sync_service_name: Name of Storage Sync Service resource.
    :type storage_sync_service_name: str
    :param server_id: Server Id
    :type server_id: str
    :param parameters: Body of Trigger Rollover request.
    :type parameters: dict | bytes

    """
    parameters = TriggerRolloverRequest.from_dict(parameters)
    return web.Response(status=200)
