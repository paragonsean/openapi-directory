from typing import List, Dict
from aiohttp import web

from openapi_server.models.query_statistic_list_result import QueryStatisticListResult
from openapi_server.models.query_text_list_result import QueryTextListResult
from openapi_server.models.top_queries_list_result import TopQueriesListResult
from openapi_server import util


async def queries_list_by_database(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name) -> web.Response:
    """queries_list_by_database

    Gets a list of top queries by database.

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


async def query_statistics_list_by_query(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, query_id) -> web.Response:
    """query_statistics_list_by_query

    Lists a query&#39;s statistics.

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
    :param query_id: The id of the query
    :type query_id: str

    """
    return web.Response(status=200)


async def query_texts_list_by_query(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, query_id) -> web.Response:
    """query_texts_list_by_query

    Gets a query&#39;s text.

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
    :param query_id: The id of the query
    :type query_id: str

    """
    return web.Response(status=200)
