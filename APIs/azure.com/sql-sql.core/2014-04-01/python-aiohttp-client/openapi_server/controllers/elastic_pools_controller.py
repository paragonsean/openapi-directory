from typing import List, Dict
from aiohttp import web

from openapi_server.models.elastic_pool_activity_list_result import ElasticPoolActivityListResult
from openapi_server.models.elastic_pool_database_activity_list_result import ElasticPoolDatabaseActivityListResult
from openapi_server import util


async def elastic_pool_activities_list_by_elastic_pool(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name) -> web.Response:
    """elastic_pool_activities_list_by_elastic_pool

    Returns elastic pool activities.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: The name of the elastic pool for which to get the current activity.
    :type elastic_pool_name: str

    """
    return web.Response(status=200)


async def elastic_pool_database_activities_list_by_elastic_pool(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name) -> web.Response:
    """elastic_pool_database_activities_list_by_elastic_pool

    Returns activity on databases inside of an elastic pool.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param elastic_pool_name: The name of the elastic pool.
    :type elastic_pool_name: str

    """
    return web.Response(status=200)
