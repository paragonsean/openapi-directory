from typing import List, Dict
from aiohttp import web

from openapi_server.models.io_t_security_aggregated_alert import IoTSecurityAggregatedAlert
from openapi_server.models.io_t_security_aggregated_alert_list import IoTSecurityAggregatedAlertList
from openapi_server.models.io_t_security_aggregated_recommendation import IoTSecurityAggregatedRecommendation
from openapi_server.models.io_t_security_aggregated_recommendation_list import IoTSecurityAggregatedRecommendationList
from openapi_server.models.io_t_security_solution_analytics_model import IoTSecuritySolutionAnalyticsModel
from openapi_server.models.io_t_security_solution_analytics_model_list import IoTSecuritySolutionAnalyticsModelList
from openapi_server.models.io_t_security_solutions_analytics_get_all_default_response import IoTSecuritySolutionsAnalyticsGetAllDefaultResponse
from openapi_server import util


async def io_t_security_solutions_analytics_aggregated_alert_dismiss(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, aggregated_alert_name) -> web.Response:
    """io_t_security_solutions_analytics_aggregated_alert_dismiss

    Security Analytics of a security solution

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The solution manager name
    :type solution_name: str
    :param aggregated_alert_name: Identifier of the aggregated alert
    :type aggregated_alert_name: str

    """
    return web.Response(status=200)


async def io_t_security_solutions_analytics_aggregated_alert_get(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, aggregated_alert_name) -> web.Response:
    """io_t_security_solutions_analytics_aggregated_alert_get

    Security Analytics of a security solution

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The solution manager name
    :type solution_name: str
    :param aggregated_alert_name: Identifier of the aggregated alert
    :type aggregated_alert_name: str

    """
    return web.Response(status=200)


async def io_t_security_solutions_analytics_aggregated_alerts_list(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, top=None) -> web.Response:
    """io_t_security_solutions_analytics_aggregated_alerts_list

    Security Analytics of a security solution

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The solution manager name
    :type solution_name: str
    :param top: The number of results to retrieve.
    :type top: int

    """
    return web.Response(status=200)


async def io_t_security_solutions_analytics_get_all(request: web.Request, api_version, subscription_id, resource_group_name, solution_name) -> web.Response:
    """io_t_security_solutions_analytics_get_all

    Security Analytics of a security solution

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The solution manager name
    :type solution_name: str

    """
    return web.Response(status=200)


async def io_t_security_solutions_analytics_get_default(request: web.Request, api_version, subscription_id, resource_group_name, solution_name) -> web.Response:
    """io_t_security_solutions_analytics_get_default

    Security Analytics of a security solution

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The solution manager name
    :type solution_name: str

    """
    return web.Response(status=200)


async def io_t_security_solutions_analytics_recommendation_get(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, aggregated_recommendation_name) -> web.Response:
    """io_t_security_solutions_analytics_recommendation_get

    Security Analytics of a security solution

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The solution manager name
    :type solution_name: str
    :param aggregated_recommendation_name: Identifier of the aggregated recommendation
    :type aggregated_recommendation_name: str

    """
    return web.Response(status=200)


async def io_t_security_solutions_analytics_recommendations_list(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, top=None) -> web.Response:
    """io_t_security_solutions_analytics_recommendations_list

    Security Analytics of a security solution

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The solution manager name
    :type solution_name: str
    :param top: The number of results to retrieve.
    :type top: int

    """
    return web.Response(status=200)
