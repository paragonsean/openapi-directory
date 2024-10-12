from typing import List, Dict
from aiohttp import web

from openapi_server.models.database import Database
from openapi_server.models.database_list_result import DatabaseListResult
from openapi_server.models.database_update import DatabaseUpdate
from openapi_server.models.resource_move_definition import ResourceMoveDefinition
from openapi_server import util


async def databases_create_or_update(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version, parameters) -> web.Response:
    """databases_create_or_update

    Creates a new database or updates an existing database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested database resource state.
    :type parameters: dict | bytes

    """
    parameters = Database.from_dict(parameters)
    return web.Response(status=200)


async def databases_delete(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """databases_delete

    Deletes the database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def databases_get(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """databases_get

    Gets a database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def databases_list_by_elastic_pool(request: web.Request, resource_group_name, server_name, elastic_pool_name, subscription_id, api_version) -> web.Response:
    """databases_list_by_elastic_pool

    Gets a list of databases in an elastic pool.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: The name of the elastic pool.
    :type elastic_pool_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def databases_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """databases_list_by_server

    Gets a list of databases.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def databases_pause(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """databases_pause

    Pauses a database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to be paused.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def databases_rename(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version, parameters) -> web.Response:
    """databases_rename

    Renames a database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to rename.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The resource move definition for renaming this database.
    :type parameters: dict | bytes

    """
    parameters = ResourceMoveDefinition.from_dict(parameters)
    return web.Response(status=200)


async def databases_resume(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """databases_resume

    Resumes a database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to be resumed.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def databases_update(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version, parameters) -> web.Response:
    """databases_update

    Updates an existing database.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested database resource state.
    :type parameters: dict | bytes

    """
    parameters = DatabaseUpdate.from_dict(parameters)
    return web.Response(status=200)


async def databases_upgrade_data_warehouse(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """databases_upgrade_data_warehouse

    Upgrades a data warehouse.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to be upgraded.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
