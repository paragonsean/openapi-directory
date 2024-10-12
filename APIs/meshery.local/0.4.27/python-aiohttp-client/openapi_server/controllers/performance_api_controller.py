from typing import List, Dict
from aiohttp import web

from openapi_server.models.performance_profile import PerformanceProfile
from openapi_server.models.performance_profile_parameters import PerformanceProfileParameters
from openapi_server.models.performance_profiles_api_response import PerformanceProfilesAPIResponse
from openapi_server.models.performance_results_api_response import PerformanceResultsAPIResponse
from openapi_server import util


async def id_delete_performance_profile(request: web.Request, id) -> web.Response:
    """Handle Delete requests for performance profiles

    Deletes a performance profile with the given id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_get_all_performance_results(request: web.Request, ) -> web.Response:
    """Handles GET requests for performance results

    Returns pages of all the performance results from Remote Provider


    """
    return web.Response(status=200)


async def id_get_performance_profiles(request: web.Request, ) -> web.Response:
    """Handle GET requests for performance profiles

    Returns the list of all the performance profiles saved by the current user


    """
    return web.Response(status=200)


async def id_get_profile_results(request: web.Request, id) -> web.Response:
    """Handle GET request for results of a profile

    Fetchs pages of results from Remote Provider for the given id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_get_single_performance_profile(request: web.Request, id) -> web.Response:
    """Handle GET requests for performance results of a profile

    Returns single performance profile with the given id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_run_performance_test(request: web.Request, id) -> web.Response:
    """Handle GET request to run a performance test

    Runs the load test with the given parameters

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def id_save_performance_profile(request: web.Request, body=None) -> web.Response:
    """Handle POST requests for saving performance profile

    Save performance profile using the current provider&#39;s persistence mechanism

    :param body: 
    :type body: dict | bytes

    """
    body = PerformanceProfileParameters.from_dict(body)
    return web.Response(status=200)
