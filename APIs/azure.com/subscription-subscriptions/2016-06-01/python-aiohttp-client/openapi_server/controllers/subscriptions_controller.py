from typing import List, Dict
from aiohttp import web

from openapi_server.models.location_list_result import LocationListResult
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_list_result import SubscriptionListResult
from openapi_server import util


async def subscriptions_get(request: web.Request, subscription_id, api_version) -> web.Response:
    """subscriptions_get

    Gets details about a specified subscription.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscriptions_list(request: web.Request, api_version) -> web.Response:
    """subscriptions_list

    Gets all subscriptions for a tenant.

    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscriptions_list_locations(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all available geo-locations.

    This operation provides all the locations that are available for resource providers; however, each resource provider may support a subset of this list.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)
