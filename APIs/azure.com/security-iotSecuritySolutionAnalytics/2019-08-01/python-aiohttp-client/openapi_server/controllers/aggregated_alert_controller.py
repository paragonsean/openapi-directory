from typing import List, Dict
from aiohttp import web

from openapi_server.models.io_t_security_aggregated_alert import IoTSecurityAggregatedAlert
from openapi_server.models.io_t_security_aggregated_alert_list import IoTSecurityAggregatedAlertList
from openapi_server.models.iot_security_solution_analytics_list_default_response import IotSecuritySolutionAnalyticsListDefaultResponse
from openapi_server import util


async def iot_security_solutions_analytics_aggregated_alert_dismiss(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, aggregated_alert_name) -> web.Response:
    """iot_security_solutions_analytics_aggregated_alert_dismiss

    Use this method to dismiss an aggregated IoT Security Solution Alert.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The name of the IoT Security solution.
    :type solution_name: str
    :param aggregated_alert_name: Identifier of the aggregated alert.
    :type aggregated_alert_name: str

    """
    return web.Response(status=200)


async def iot_security_solutions_analytics_aggregated_alert_get(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, aggregated_alert_name) -> web.Response:
    """iot_security_solutions_analytics_aggregated_alert_get

    Use this method to get a single the aggregated alert of yours IoT Security solution. This aggregation is performed by alert name.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The name of the IoT Security solution.
    :type solution_name: str
    :param aggregated_alert_name: Identifier of the aggregated alert.
    :type aggregated_alert_name: str

    """
    return web.Response(status=200)


async def iot_security_solutions_analytics_aggregated_alert_list(request: web.Request, api_version, subscription_id, resource_group_name, solution_name, top=None) -> web.Response:
    """iot_security_solutions_analytics_aggregated_alert_list

    Use this method to get the aggregated alert list of yours IoT Security solution.

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
