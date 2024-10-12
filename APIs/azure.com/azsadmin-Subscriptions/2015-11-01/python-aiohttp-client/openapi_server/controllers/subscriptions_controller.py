from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_list import SubscriptionList
from openapi_server import util


async def subscriptions_create_or_update(request: web.Request, subscription_id, api_version, new_subscription) -> web.Response:
    """subscriptions_create_or_update

    Create or updates a subscription.

    :param subscription_id: Id of the subscription.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param new_subscription: Subscription parameter.
    :type new_subscription: dict | bytes

    """
    new_subscription = Subscription.from_dict(new_subscription)
    return web.Response(status=200)


async def subscriptions_delete(request: web.Request, subscription_id, api_version) -> web.Response:
    """subscriptions_delete

    Delete the specified subscription.

    :param subscription_id: Id of the subscription.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscriptions_get(request: web.Request, subscription_id, api_version) -> web.Response:
    """subscriptions_get

    Gets details about particular subscription.

    :param subscription_id: Id of the subscription.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscriptions_list(request: web.Request, api_version) -> web.Response:
    """subscriptions_list

    Get the list of subscriptions.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
