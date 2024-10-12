from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_usage import SubscriptionUsage
from openapi_server.models.subscription_usage_list_result import SubscriptionUsageListResult
from openapi_server import util


async def subscription_usages_get(request: web.Request, location_name, usage_name, subscription_id, api_version) -> web.Response:
    """subscription_usages_get

    Gets a subscription usage metric.

    :param location_name: The name of the region where the resource is located.
    :type location_name: str
    :param usage_name: Name of usage metric to return.
    :type usage_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscription_usages_list_by_location(request: web.Request, location_name, subscription_id, api_version) -> web.Response:
    """subscription_usages_list_by_location

    Gets all subscription usage metrics in a given location.

    :param location_name: The name of the region where the resource is located.
    :type location_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
