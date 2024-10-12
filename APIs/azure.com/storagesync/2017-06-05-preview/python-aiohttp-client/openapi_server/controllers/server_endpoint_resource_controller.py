from typing import List, Dict
from aiohttp import web

from openapi_server.models.server_endpoint import ServerEndpoint
from openapi_server.models.server_endpoint_array import ServerEndpointArray
from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server import util


async def server_endpoints_create(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, server_endpoint_name, parameters) -> web.Response:
    """server_endpoints_create

    Create a new ServerEndpoint.

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
    :param server_endpoint_name: Name of Server Endpoint object.
    :type server_endpoint_name: str
    :param parameters: Body of Server Endpoint object.
    :type parameters: dict | bytes

    """
    parameters = ServerEndpoint.from_dict(parameters)
    return web.Response(status=200)


async def server_endpoints_delete(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, server_endpoint_name) -> web.Response:
    """server_endpoints_delete

    Delete a given ServerEndpoint.

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
    :param server_endpoint_name: Name of Server Endpoint object.
    :type server_endpoint_name: str

    """
    return web.Response(status=200)


async def server_endpoints_get(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, server_endpoint_name) -> web.Response:
    """server_endpoints_get

    Get a ServerEndpoint.

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
    :param server_endpoint_name: Name of Server Endpoint object.
    :type server_endpoint_name: str

    """
    return web.Response(status=200)


async def server_endpoints_list_by_sync_group(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name) -> web.Response:
    """server_endpoints_list_by_sync_group

    Get a ServerEndpoint list.

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


async def server_endpoints_recall(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, server_endpoint_name) -> web.Response:
    """server_endpoints_recall

    Recall a server endpoint.

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
    :param server_endpoint_name: Name of Server Endpoint object.
    :type server_endpoint_name: str

    """
    return web.Response(status=200)


async def server_endpoints_update(request: web.Request, subscription_id, resource_group_name, api_version, storage_sync_service_name, sync_group_name, server_endpoint_name, parameters=None) -> web.Response:
    """server_endpoints_update

    Patch a given ServerEndpoint.

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
    :param server_endpoint_name: Name of Server Endpoint object.
    :type server_endpoint_name: str
    :param parameters: Any of the properties applicable in PUT request.
    :type parameters: dict | bytes

    """
    parameters = ServerEndpoint.from_dict(parameters)
    return web.Response(status=200)
