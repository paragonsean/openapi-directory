from typing import List, Dict
from aiohttp import web

from openapi_server.models.daily_invocation_statistic import DailyInvocationStatistic
from openapi_server.models.test_conformance_metric import TestConformanceMetric
from openapi_server.models.test_result_summary import TestResultSummary
from openapi_server.models.weighted_metric_value import WeightedMetricValue
from openapi_server import util


async def get_aggregated_invocations_stats(request: web.Request, day=None) -> web.Response:
    """Get aggregated invocation statistics for a day

    

    :param day: The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
    :type day: str

    """
    return web.Response(status=200)


async def get_conformance_metrics_aggregation(request: web.Request, ) -> web.Response:
    """Get aggregation of conformance metrics

    


    """
    return web.Response(status=200)


async def get_invocation_stats_by_service(request: web.Request, service_name, service_version, day=None) -> web.Response:
    """Get invocation statistics for Service

    

    :param service_name: Name of service to get statistics for
    :type service_name: str
    :param service_version: Version of service to get statistics for
    :type service_version: str
    :param day: The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
    :type day: str

    """
    return web.Response(status=200)


async def get_latest_aggregated_invocations_stats(request: web.Request, limit=None) -> web.Response:
    """Get aggregated invocations statistics for latest days

    

    :param limit: Number of days to get back in time. Default is 20.
    :type limit: int

    """
    return web.Response(status=200)


async def get_latest_test_results(request: web.Request, limit=None) -> web.Response:
    """Get latest tests results

    

    :param limit: Number of days to consider for test results to return. Default is 7 (one week)
    :type limit: int

    """
    return web.Response(status=200)


async def get_service_test_conformance_metric(request: web.Request, service_id) -> web.Response:
    """Get conformance metrics for a Service

    

    :param service_id: Unique Services identifier this metrics are related to
    :type service_id: str

    """
    return web.Response(status=200)


async def get_top_ivnocations_stats_by_day(request: web.Request, day=None, limit=None) -> web.Response:
    """Get top invocation statistics for a day

    

    :param day: The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
    :type day: str
    :param limit: The number of top invoked mocks to return
    :type limit: int

    """
    return web.Response(status=200)
