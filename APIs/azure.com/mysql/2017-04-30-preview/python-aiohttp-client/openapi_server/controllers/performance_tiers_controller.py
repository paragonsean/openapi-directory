from typing import List, Dict
from aiohttp import web

from openapi_server.models.performance_tier_list_result import PerformanceTierListResult
from openapi_server import util


async def performance_tiers_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """performance_tiers_list

    List all the performance tiers in a given subscription.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
