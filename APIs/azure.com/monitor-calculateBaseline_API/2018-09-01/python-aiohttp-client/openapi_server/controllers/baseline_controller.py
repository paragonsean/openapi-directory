from typing import List, Dict
from aiohttp import web

from openapi_server.models.calculate_baseline_response import CalculateBaselineResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.time_series_information import TimeSeriesInformation
from openapi_server import util


async def metric_baseline_calculate_baseline(request: web.Request, resource_uri, api_version, time_series_information) -> web.Response:
    """metric_baseline_calculate_baseline

    **Lists the baseline values for a resource**.

    :param resource_uri: The identifier of the resource. It has the following structure: subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}. For example: subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param time_series_information: Information that need to be specified to calculate a baseline on a time series.
    :type time_series_information: dict | bytes

    """
    time_series_information = TimeSeriesInformation.from_dict(time_series_information)
    return web.Response(status=200)
