from typing import List, Dict
from aiohttp import web

from openapi_server.models.sync_database_id_list_result import SyncDatabaseIdListResult
from openapi_server.models.sync_full_schema_properties_list_result import SyncFullSchemaPropertiesListResult
from openapi_server.models.sync_group import SyncGroup
from openapi_server.models.sync_group_list_result import SyncGroupListResult
from openapi_server.models.sync_group_log_list_result import SyncGroupLogListResult
from openapi_server import util


async def sync_groups_cancel_sync(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, subscription_id, api_version) -> web.Response:
    """sync_groups_cancel_sync

    Cancels a sync group synchronization.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_groups_create_or_update(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, subscription_id, api_version, parameters) -> web.Response:
    """sync_groups_create_or_update

    Creates or updates a sync group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested sync group resource state.
    :type parameters: dict | bytes

    """
    parameters = SyncGroup.from_dict(parameters)
    return web.Response(status=200)


async def sync_groups_delete(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, subscription_id, api_version) -> web.Response:
    """sync_groups_delete

    Deletes a sync group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_groups_get(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, subscription_id, api_version) -> web.Response:
    """sync_groups_get

    Gets a sync group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_groups_list_by_database(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """sync_groups_list_by_database

    Lists sync groups under a hub database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_groups_list_hub_schemas(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, subscription_id, api_version) -> web.Response:
    """sync_groups_list_hub_schemas

    Gets a collection of hub database schemas.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_groups_list_logs(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, start_time, end_time, type, subscription_id, api_version, continuation_token=None) -> web.Response:
    """sync_groups_list_logs

    Gets a collection of sync group logs.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param start_time: Get logs generated after this time.
    :type start_time: str
    :param end_time: Get logs generated before this time.
    :type end_time: str
    :param type: The types of logs to retrieve.
    :type type: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param continuation_token: The continuation token for this operation.
    :type continuation_token: str

    """
    return web.Response(status=200)


async def sync_groups_list_sync_database_ids(request: web.Request, location_name, subscription_id, api_version) -> web.Response:
    """sync_groups_list_sync_database_ids

    Gets a collection of sync database ids.

    :param location_name: The name of the region where the resource is located.
    :type location_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_groups_refresh_hub_schema(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, subscription_id, api_version) -> web.Response:
    """sync_groups_refresh_hub_schema

    Refreshes a hub database schema.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_groups_trigger_sync(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, subscription_id, api_version) -> web.Response:
    """sync_groups_trigger_sync

    Triggers a sync group synchronization.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def sync_groups_update(request: web.Request, resource_group_name, server_name, database_name, sync_group_name, subscription_id, api_version, parameters) -> web.Response:
    """sync_groups_update

    Updates a sync group.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database on which the sync group is hosted.
    :type database_name: str
    :param sync_group_name: The name of the sync group.
    :type sync_group_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested sync group resource state.
    :type parameters: dict | bytes

    """
    parameters = SyncGroup.from_dict(parameters)
    return web.Response(status=200)
