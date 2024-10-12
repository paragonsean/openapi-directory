from typing import List, Dict
from aiohttp import web

from openapi_server.models.long_term_retention_backup import LongTermRetentionBackup
from openapi_server.models.long_term_retention_backup_list_result import LongTermRetentionBackupListResult
from openapi_server import util


async def long_term_retention_backups_delete(request: web.Request, location_name, long_term_retention_server_name, long_term_retention_database_name, backup_name, subscription_id, api_version) -> web.Response:
    """long_term_retention_backups_delete

    Deletes a long term retention backup.

    :param location_name: The location of the database
    :type location_name: str
    :param long_term_retention_server_name: The name of the server
    :type long_term_retention_server_name: str
    :param long_term_retention_database_name: The name of the database
    :type long_term_retention_database_name: str
    :param backup_name: The backup name.
    :type backup_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def long_term_retention_backups_delete_by_resource_group(request: web.Request, resource_group_name, location_name, long_term_retention_server_name, long_term_retention_database_name, backup_name, subscription_id, api_version) -> web.Response:
    """long_term_retention_backups_delete_by_resource_group

    Deletes a long term retention backup.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The location of the database
    :type location_name: str
    :param long_term_retention_server_name: The name of the server
    :type long_term_retention_server_name: str
    :param long_term_retention_database_name: The name of the database
    :type long_term_retention_database_name: str
    :param backup_name: The backup name.
    :type backup_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def long_term_retention_backups_get(request: web.Request, location_name, long_term_retention_server_name, long_term_retention_database_name, backup_name, subscription_id, api_version) -> web.Response:
    """long_term_retention_backups_get

    Gets a long term retention backup.

    :param location_name: The location of the database.
    :type location_name: str
    :param long_term_retention_server_name: The name of the server
    :type long_term_retention_server_name: str
    :param long_term_retention_database_name: The name of the database
    :type long_term_retention_database_name: str
    :param backup_name: The backup name.
    :type backup_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def long_term_retention_backups_get_by_resource_group(request: web.Request, resource_group_name, location_name, long_term_retention_server_name, long_term_retention_database_name, backup_name, subscription_id, api_version) -> web.Response:
    """long_term_retention_backups_get_by_resource_group

    Gets a long term retention backup.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The location of the database.
    :type location_name: str
    :param long_term_retention_server_name: The name of the server
    :type long_term_retention_server_name: str
    :param long_term_retention_database_name: The name of the database
    :type long_term_retention_database_name: str
    :param backup_name: The backup name.
    :type backup_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def long_term_retention_backups_list_by_database(request: web.Request, location_name, long_term_retention_server_name, long_term_retention_database_name, subscription_id, api_version, only_latest_per_database=None, database_state=None) -> web.Response:
    """long_term_retention_backups_list_by_database

    Lists all long term retention backups for a database.

    :param location_name: The location of the database
    :type location_name: str
    :param long_term_retention_server_name: The name of the server
    :type long_term_retention_server_name: str
    :param long_term_retention_database_name: The name of the database
    :type long_term_retention_database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param only_latest_per_database: Whether or not to only get the latest backup for each database.
    :type only_latest_per_database: bool
    :param database_state: Whether to query against just live databases, just deleted databases, or all databases.
    :type database_state: str

    """
    return web.Response(status=200)


async def long_term_retention_backups_list_by_location(request: web.Request, location_name, subscription_id, api_version, only_latest_per_database=None, database_state=None) -> web.Response:
    """long_term_retention_backups_list_by_location

    Lists the long term retention backups for a given location.

    :param location_name: The location of the database
    :type location_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param only_latest_per_database: Whether or not to only get the latest backup for each database.
    :type only_latest_per_database: bool
    :param database_state: Whether to query against just live databases, just deleted databases, or all databases.
    :type database_state: str

    """
    return web.Response(status=200)


async def long_term_retention_backups_list_by_resource_group_database(request: web.Request, resource_group_name, location_name, long_term_retention_server_name, long_term_retention_database_name, subscription_id, api_version, only_latest_per_database=None, database_state=None) -> web.Response:
    """long_term_retention_backups_list_by_resource_group_database

    Lists all long term retention backups for a database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The location of the database
    :type location_name: str
    :param long_term_retention_server_name: The name of the server
    :type long_term_retention_server_name: str
    :param long_term_retention_database_name: The name of the database
    :type long_term_retention_database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param only_latest_per_database: Whether or not to only get the latest backup for each database.
    :type only_latest_per_database: bool
    :param database_state: Whether to query against just live databases, just deleted databases, or all databases.
    :type database_state: str

    """
    return web.Response(status=200)


async def long_term_retention_backups_list_by_resource_group_location(request: web.Request, resource_group_name, location_name, subscription_id, api_version, only_latest_per_database=None, database_state=None) -> web.Response:
    """long_term_retention_backups_list_by_resource_group_location

    Lists the long term retention backups for a given location.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The location of the database
    :type location_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param only_latest_per_database: Whether or not to only get the latest backup for each database.
    :type only_latest_per_database: bool
    :param database_state: Whether to query against just live databases, just deleted databases, or all databases.
    :type database_state: str

    """
    return web.Response(status=200)


async def long_term_retention_backups_list_by_resource_group_server(request: web.Request, resource_group_name, location_name, long_term_retention_server_name, subscription_id, api_version, only_latest_per_database=None, database_state=None) -> web.Response:
    """long_term_retention_backups_list_by_resource_group_server

    Lists the long term retention backups for a given server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param location_name: The location of the database
    :type location_name: str
    :param long_term_retention_server_name: The name of the server
    :type long_term_retention_server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param only_latest_per_database: Whether or not to only get the latest backup for each database.
    :type only_latest_per_database: bool
    :param database_state: Whether to query against just live databases, just deleted databases, or all databases.
    :type database_state: str

    """
    return web.Response(status=200)


async def long_term_retention_backups_list_by_server(request: web.Request, location_name, long_term_retention_server_name, subscription_id, api_version, only_latest_per_database=None, database_state=None) -> web.Response:
    """long_term_retention_backups_list_by_server

    Lists the long term retention backups for a given server.

    :param location_name: The location of the database
    :type location_name: str
    :param long_term_retention_server_name: The name of the server
    :type long_term_retention_server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param only_latest_per_database: Whether or not to only get the latest backup for each database.
    :type only_latest_per_database: bool
    :param database_state: Whether to query against just live databases, just deleted databases, or all databases.
    :type database_state: str

    """
    return web.Response(status=200)
