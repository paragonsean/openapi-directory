from typing import List, Dict
from aiohttp import web

from openapi_server.models.io_t_security_solution_analytics_model import IoTSecuritySolutionAnalyticsModel
from openapi_server.models.io_t_security_solution_analytics_model_list import IoTSecuritySolutionAnalyticsModelList
from openapi_server.models.iot_security_solution_analytics_list_default_response import IotSecuritySolutionAnalyticsListDefaultResponse
from openapi_server import util


async def iot_security_solution_analytics_get(request: web.Request, api_version, subscription_id, resource_group_name, solution_name) -> web.Response:
    """iot_security_solution_analytics_get

    Use this method to get IoT Security Analytics metrics.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The name of the IoT Security solution.
    :type solution_name: str

    """
    return web.Response(status=200)


async def iot_security_solution_analytics_list(request: web.Request, api_version, subscription_id, resource_group_name, solution_name) -> web.Response:
    """iot_security_solution_analytics_list

    Use this method to get IoT security Analytics metrics in an array.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param solution_name: The name of the IoT Security solution.
    :type solution_name: str

    """
    return web.Response(status=200)
