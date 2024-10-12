from typing import List, Dict
from aiohttp import web

from openapi_server.models.performance_tier_list_result import PerformanceTierListResult
from openapi_server import util


async def location_based_performance_tier_list(request: web.Request, api_version, subscription_id, location_name) -> web.Response:
    """location_based_performance_tier_list

    List all the performance tiers at specified location in a given subscription.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param location_name: The name of the location.
    :type location_name: str

    """
    return web.Response(status=200)
