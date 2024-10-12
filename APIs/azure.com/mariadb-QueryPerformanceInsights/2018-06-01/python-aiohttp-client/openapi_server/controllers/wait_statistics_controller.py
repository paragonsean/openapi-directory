from typing import List, Dict
from aiohttp import web

from openapi_server.models.wait_statistic import WaitStatistic
from openapi_server.models.wait_statistics_input import WaitStatisticsInput
from openapi_server.models.wait_statistics_result_list import WaitStatisticsResultList
from openapi_server import util


async def wait_statistics_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, wait_statistics_id) -> web.Response:
    """wait_statistics_get

    Retrieve wait statistics for specified identifier.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param wait_statistics_id: The Wait Statistic identifier.
    :type wait_statistics_id: str

    """
    return web.Response(status=200)


async def wait_statistics_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name, parameters) -> web.Response:
    """wait_statistics_list_by_server

    Retrieve wait statistics for specified aggregation window.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param parameters: The required parameters for retrieving wait statistics.
    :type parameters: dict | bytes

    """
    parameters = WaitStatisticsInput.from_dict(parameters)
    return web.Response(status=200)
