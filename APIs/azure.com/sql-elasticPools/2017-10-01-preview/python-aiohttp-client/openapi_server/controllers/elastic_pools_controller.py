from typing import List, Dict
from aiohttp import web

from openapi_server.models.elastic_pool import ElasticPool
from openapi_server.models.elastic_pool_list_result import ElasticPoolListResult
from openapi_server.models.elastic_pool_update import ElasticPoolUpdate
from openapi_server import util


async def elastic_pools_create_or_update(request: web.Request, resource_group_name, server_name, elastic_pool_name, subscription_id, api_version, parameters) -> web.Response:
    """elastic_pools_create_or_update

    Creates or updates an elastic pool.

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
    :param parameters: The elastic pool parameters.
    :type parameters: dict | bytes

    """
    parameters = ElasticPool.from_dict(parameters)
    return web.Response(status=200)


async def elastic_pools_delete(request: web.Request, resource_group_name, server_name, elastic_pool_name, subscription_id, api_version) -> web.Response:
    """elastic_pools_delete

    Deletes an elastic pool.

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


async def elastic_pools_get(request: web.Request, resource_group_name, server_name, elastic_pool_name, subscription_id, api_version) -> web.Response:
    """elastic_pools_get

    Gets an elastic pool.

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


async def elastic_pools_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version, skip=None) -> web.Response:
    """elastic_pools_list_by_server

    Gets all elastic pools in a server.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param skip: The number of elements in the collection to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def elastic_pools_update(request: web.Request, resource_group_name, server_name, elastic_pool_name, subscription_id, api_version, parameters) -> web.Response:
    """elastic_pools_update

    Updates an elastic pool.

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
    :param parameters: The elastic pool update parameters.
    :type parameters: dict | bytes

    """
    parameters = ElasticPoolUpdate.from_dict(parameters)
    return web.Response(status=200)
