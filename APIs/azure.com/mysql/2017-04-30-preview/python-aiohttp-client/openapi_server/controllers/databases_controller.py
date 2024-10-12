from typing import List, Dict
from aiohttp import web

from openapi_server.models.database import Database
from openapi_server.models.database_list_result import DatabaseListResult
from openapi_server import util


async def databases_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, parameters) -> web.Response:
    """databases_create_or_update

    Creates a new database or updates an existing database.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param parameters: The required parameters for creating or updating a database.
    :type parameters: dict | bytes

    """
    parameters = Database.from_dict(parameters)
    return web.Response(status=200)


async def databases_delete(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name) -> web.Response:
    """databases_delete

    Deletes a database.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str

    """
    return web.Response(status=200)


async def databases_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name) -> web.Response:
    """databases_get

    Gets information about a database.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str

    """
    return web.Response(status=200)


async def databases_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """databases_list_by_server

    List all the databases in a given server.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str

    """
    return web.Response(status=200)
