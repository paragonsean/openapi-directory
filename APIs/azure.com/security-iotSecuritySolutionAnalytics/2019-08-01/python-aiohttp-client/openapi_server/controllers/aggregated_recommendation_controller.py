from typing import List, Dict
from aiohttp import web

from openapi_server.models.io_t_security_aggregated_recommendation import IoTSecurityAggregatedRecommendation
from openapi_server.models.io_t_security_aggregated_recommendation_list import IoTSecurityAggregatedRecommendationList
from openapi_server.models.iot_security_solution_analytics_list_default_response import IotSecuritySolutionAnalyticsListDefaultResponse
from openapi_server import util


async def iot_security_solutions_analytics_recommendation_get(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, aggregated_recommendation_name) -> web.Response:
    """iot_security_solutions_analytics_recommendation_get

    Use this method to get the aggregated security analytics recommendation of yours IoT Security solution. This aggregation is performed by recommendation name.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The name of the IoT Security solution.
    :type solution_name: str
    :param aggregated_recommendation_name: Name of the recommendation aggregated for this query.
    :type aggregated_recommendation_name: str

    """
    return web.Response(status=200)


async def iot_security_solutions_analytics_recommendation_list(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, top=None) -> web.Response:
    """iot_security_solutions_analytics_recommendation_list

    Use this method to get the list of aggregated security analytics recommendations of yours IoT Security solution.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The name of the IoT Security solution.
    :type solution_name: str
    :param top: Number of results to retrieve.
    :type top: int

    """
    return web.Response(status=200)
