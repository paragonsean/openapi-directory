from typing import List, Dict
from aiohttp import web

from openapi_server.models.log_analytics_operation_result import LogAnalyticsOperationResult
from openapi_server.models.request_rate_by_interval_input import RequestRateByIntervalInput
from openapi_server.models.throttled_requests_input import ThrottledRequestsInput
from openapi_server import util


async def log_analytics_export_request_rate_by_interval(request: web.Request, location, api_version, subscription_id, parameters) -> web.Response:
    """log_analytics_export_request_rate_by_interval

    Export logs that show Api requests made by this subscription in the given time window to show throttling activities.

    :param location: The location upon which virtual-machine-sizes is queried.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the LogAnalytics getRequestRateByInterval Api.
    :type parameters: dict | bytes

    """
    parameters = RequestRateByIntervalInput.from_dict(parameters)
    return web.Response(status=200)


async def log_analytics_export_throttled_requests(request: web.Request, location, api_version, subscription_id, parameters) -> web.Response:
    """log_analytics_export_throttled_requests

    Export logs that show total throttled Api requests for this subscription in the given time window.

    :param location: The location upon which virtual-machine-sizes is queried.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the LogAnalytics getThrottledRequests Api.
    :type parameters: dict | bytes

    """
    parameters = ThrottledRequestsInput.from_dict(parameters)
    return web.Response(status=200)
