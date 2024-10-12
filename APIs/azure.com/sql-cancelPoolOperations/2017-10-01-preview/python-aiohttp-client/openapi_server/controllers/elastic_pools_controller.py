from typing import List, Dict
from aiohttp import web

from openapi_server.models.elastic_pool_operation_list_result import ElasticPoolOperationListResult
from openapi_server import util


async def elastic_pool_operations_cancel(request: web.Request, resource_group_name, server_name, elastic_pool_name, operation_id, subscription_id, api_version) -> web.Response:
    """elastic_pool_operations_cancel

    Cancels the asynchronous operation on the elastic pool.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: 
    :type elastic_pool_name: str
    :param operation_id: The operation identifier.
    :type operation_id: str
    :type operation_id: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def elastic_pool_operations_list_by_elastic_pool(request: web.Request, resource_group_name, server_name, elastic_pool_name, subscription_id, api_version) -> web.Response:
    """elastic_pool_operations_list_by_elastic_pool

    Gets a list of operations performed on the elastic pool.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: 
    :type elastic_pool_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
