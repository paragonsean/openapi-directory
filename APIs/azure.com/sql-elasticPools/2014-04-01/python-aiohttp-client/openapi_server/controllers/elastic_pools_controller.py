from typing import List, Dict
from aiohttp import web

from openapi_server.models.elastic_pool import ElasticPool
from openapi_server.models.elastic_pool_list_result import ElasticPoolListResult
from openapi_server.models.elastic_pool_update import ElasticPoolUpdate
from openapi_server import util


async def elastic_pools_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name, parameters) -> web.Response:
    """elastic_pools_create_or_update

    Creates a new elastic pool or updates an existing elastic pool.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: The name of the elastic pool to be operated on (updated or created).
    :type elastic_pool_name: str
    :param parameters: The required parameters for creating or updating an elastic pool.
    :type parameters: dict | bytes

    """
    parameters = ElasticPool.from_dict(parameters)
    return web.Response(status=200)


async def elastic_pools_delete(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name) -> web.Response:
    """elastic_pools_delete

    Deletes the elastic pool.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: The name of the elastic pool to be deleted.
    :type elastic_pool_name: str

    """
    return web.Response(status=200)


async def elastic_pools_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name) -> web.Response:
    """elastic_pools_get

    Gets an elastic pool.

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


async def elastic_pools_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """elastic_pools_list_by_server

    Returns a list of elastic pools in a server.

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


async def elastic_pools_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name, parameters) -> web.Response:
    """elastic_pools_update

    Updates an existing elastic pool.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: The name of the elastic pool to be updated.
    :type elastic_pool_name: str
    :param parameters: The required parameters for updating an elastic pool.
    :type parameters: dict | bytes

    """
    parameters = ElasticPoolUpdate.from_dict(parameters)
    return web.Response(status=200)
