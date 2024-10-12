from typing import List, Dict
from aiohttp import web

from openapi_server.models.performance_results_api_response import PerformanceResultsAPIResponse
from openapi_server.models.performance_spec import PerformanceSpec
from openapi_server.models.performance_test_config import PerformanceTestConfig
from openapi_server import util


async def id_get_all_perf_results(request: web.Request, ) -> web.Response:
    """Handles GET requests for perf results

    Returns pages of all the perf results from Remote Provider


    """
    return web.Response(status=200)


async def id_get_single_perf_result(request: web.Request, id) -> web.Response:
    """Handles GET requests for perf result

    Returns an individual result from provider

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def id_run_perf_test(request: web.Request, body=None) -> web.Response:
    """Handle GET request to run a test

    Runs the load test with the given parameters

    :param body: 
    :type body: dict | bytes

    """
    body = PerformanceTestConfig.from_dict(body)
    return web.Response(status=200)
