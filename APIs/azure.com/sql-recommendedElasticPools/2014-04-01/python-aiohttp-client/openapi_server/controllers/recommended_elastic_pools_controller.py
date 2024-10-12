from typing import List, Dict
from aiohttp import web

from openapi_server.models.recommended_elastic_pool import RecommendedElasticPool
from openapi_server.models.recommended_elastic_pool_list_metrics_result import RecommendedElasticPoolListMetricsResult
from openapi_server.models.recommended_elastic_pool_list_result import RecommendedElasticPoolListResult
from openapi_server import util


async def recommended_elastic_pools_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, recommended_elastic_pool_name) -> web.Response:
    """recommended_elastic_pools_get

    Gets a recommended elastic pool.

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


async def recommended_elastic_pools_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """recommended_elastic_pools_list_by_server

    Returns recommended elastic pools.

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


async def recommended_elastic_pools_list_metrics(request: web.Request, api_version, subscription_id, resource_group_name, server_name, recommended_elastic_pool_name) -> web.Response:
    """recommended_elastic_pools_list_metrics

    Returns recommended elastic pool metrics.

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
