from typing import List, Dict
from aiohttp import web

from openapi_server.models.canceled_subscription_id import CanceledSubscriptionId
from openapi_server.models.enabled_subscription_id import EnabledSubscriptionId
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.renamed_subscription_id import RenamedSubscriptionId
from openapi_server.models.subscription_name import SubscriptionName
from openapi_server import util


async def subscriptions_cancel(request: web.Request, subscription_id, api_version) -> web.Response:
    """subscriptions_cancel

    The operation to cancel a subscription

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2019-03-01-preview
    :type api_version: str

    """
    return web.Response(status=200)


async def subscriptions_enable(request: web.Request, subscription_id, api_version) -> web.Response:
    """subscriptions_enable

    The operation to enable a subscription

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2019-03-01-preview
    :type api_version: str

    """
    return web.Response(status=200)


async def subscriptions_rename(request: web.Request, subscription_id, api_version, body) -> web.Response:
    """subscriptions_rename

    The operation to rename a subscription

    :param subscription_id: Subscription Id.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2019-03-01-preview
    :type api_version: str
    :param body: Subscription Name
    :type body: dict | bytes

    """
    body = SubscriptionName.from_dict(body)
    return web.Response(status=200)
