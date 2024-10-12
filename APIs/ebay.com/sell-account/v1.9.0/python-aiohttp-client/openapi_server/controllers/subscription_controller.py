from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_response import SubscriptionResponse
from openapi_server import util


async def get_subscription(request: web.Request, limit=None, continuation_token=None) -> web.Response:
    """get_subscription

    This method retrieves a list of subscriptions associated with the seller account.

    :param limit: This field is for future use.
    :type limit: str
    :param continuation_token: This field is for future use.
    :type continuation_token: str

    """
    return web.Response(status=200)
