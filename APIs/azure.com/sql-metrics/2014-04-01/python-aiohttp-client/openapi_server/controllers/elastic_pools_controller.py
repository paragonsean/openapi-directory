from typing import List, Dict
from aiohttp import web

from openapi_server.models.metric_definition_list_result import MetricDefinitionListResult
from openapi_server.models.metric_list_result import MetricListResult
from openapi_server import util


async def elastic_pools_list_metric_definitions(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name) -> web.Response:
    """elastic_pools_list_metric_definitions

    Returns elastic pool metric definitions.

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


async def elastic_pools_list_metrics(request: web.Request, api_version, subscription_id, resource_group_name, server_name, elastic_pool_name, filter) -> web.Response:
    """elastic_pools_list_metrics

    Returns elastic pool  metrics.

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
    :param filter: An OData filter expression that describes a subset of metrics to return.
    :type filter: str

    """
    return web.Response(status=200)
