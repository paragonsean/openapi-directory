from typing import List, Dict
from aiohttp import web

from openapi_server.models.database import Database
from openapi_server.models.database_list_result import DatabaseListResult
from openapi_server.models.database_update import DatabaseUpdate
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
    :param database_name: The name of the database to be operated on (updated or created).
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
    :param database_name: The name of the database to be deleted.
    :type database_name: str

    """
    return web.Response(status=200)


async def databases_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, expand=None) -> web.Response:
    """databases_get

    Gets a database.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to be retrieved.
    :type database_name: str
    :param expand: A comma separated list of child objects to expand in the response. Possible properties: serviceTierAdvisors, transparentDataEncryption.
    :type expand: str

    """
    return web.Response(status=200)


async def databases_get_by_recommended_elastic_pool(request: web.Request, api_version, subscription_id, resource_group_name, server_name, recommended_elastic_pool_name, database_name) -> web.Response:
    """databases_get_by_recommended_elastic_pool

    Gets a database inside of a recommended elastic pool.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param recommended_elastic_pool_name: The name of the elastic pool to be retrieved.
    :type recommended_elastic_pool_name: str
    :param database_name: The name of the database to be retrieved.
    :type database_name: str

    """
    return web.Response(status=200)


async def databases_list_by_elastic_pool(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name) -> web.Response:
    """databases_list_by_elastic_pool

    Returns a list of databases in an elastic pool.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: The name of the elastic pool to be retrieved.
    :type elastic_pool_name: str

    """
    return web.Response(status=200)


async def databases_list_by_recommended_elastic_pool(request: web.Request, api_version, subscription_id, resource_group_name, server_name, recommended_elastic_pool_name) -> web.Response:
    """databases_list_by_recommended_elastic_pool

    Returns a list of databases inside a recommended elastic pool.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param recommended_elastic_pool_name: The name of the recommended elastic pool to be retrieved.
    :type recommended_elastic_pool_name: str

    """
    return web.Response(status=200)


async def databases_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name, expand=None, filter=None) -> web.Response:
    """databases_list_by_server

    Returns a list of databases in a server.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param expand: A comma separated list of child objects to expand in the response. Possible properties: serviceTierAdvisors, transparentDataEncryption.
    :type expand: str
    :param filter: An OData filter expression that describes a subset of databases to return.
    :type filter: str

    """
    return web.Response(status=200)


async def databases_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, parameters) -> web.Response:
    """databases_update

    Updates an existing database.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database to be updated.
    :type database_name: str
    :param parameters: The required parameters for updating a database.
    :type parameters: dict | bytes

    """
    parameters = DatabaseUpdate.from_dict(parameters)
    return web.Response(status=200)
