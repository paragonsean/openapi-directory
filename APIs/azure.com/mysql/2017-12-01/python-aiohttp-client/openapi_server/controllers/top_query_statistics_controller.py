from typing import List, Dict
from aiohttp import web

from openapi_server.models.query_statistic import QueryStatistic
from openapi_server.models.top_query_statistics_input import TopQueryStatisticsInput
from openapi_server.models.top_query_statistics_result_list import TopQueryStatisticsResultList
from openapi_server import util


async def top_query_statistics_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, query_statistic_id) -> web.Response:
    """top_query_statistics_get

    Retrieve the query statistic for specified identifier.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param query_statistic_id: The Query Statistic identifier.
    :type query_statistic_id: str

    """
    return web.Response(status=200)


async def top_query_statistics_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name, parameters) -> web.Response:
    """top_query_statistics_list_by_server

    Retrieve the Query-Store top queries for specified metric and aggregation.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param parameters: The required parameters for retrieving top query statistics.
    :type parameters: dict | bytes

    """
    parameters = TopQueryStatisticsInput.from_dict(parameters)
    return web.Response(status=200)
