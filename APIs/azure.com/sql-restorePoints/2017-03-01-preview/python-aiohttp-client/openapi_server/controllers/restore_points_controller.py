from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_database_restore_point_definition import CreateDatabaseRestorePointDefinition
from openapi_server.models.restore_point import RestorePoint
from openapi_server.models.restore_point_list_result import RestorePointListResult
from openapi_server import util


async def restore_points_create(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version, parameters) -> web.Response:
    """restore_points_create

    Creates a restore point for a data warehouse.

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
    :param parameters: The definition for creating the restore point of this database.
    :type parameters: dict | bytes

    """
    parameters = CreateDatabaseRestorePointDefinition.from_dict(parameters)
    return web.Response(status=200)


async def restore_points_delete(request: web.Request, resource_group_name, server_name, database_name, restore_point_name, subscription_id, api_version) -> web.Response:
    """restore_points_delete

    Deletes a restore point.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param restore_point_name: The name of the restore point.
    :type restore_point_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def restore_points_get(request: web.Request, resource_group_name, server_name, database_name, restore_point_name, subscription_id, api_version) -> web.Response:
    """restore_points_get

    Gets a restore point.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param restore_point_name: The name of the restore point.
    :type restore_point_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def restore_points_list_by_database(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """restore_points_list_by_database

    Gets a list of database restore points.

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
