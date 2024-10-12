from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_submission import SubscriptionSubmission
from openapi_server.models.subscription_type import SubscriptionType
from openapi_server import util


async def subscription_types_get(request: web.Request, ) -> web.Response:
    """Subscription types

    List available subscription types


    """
    return web.Response(status=200)


async def subscriptions_get(request: web.Request, body) -> web.Response:
    """List subscriptions for the authorised user.

    

    :param body: Subscription to be created
    :type body: dict | bytes

    """
    body = SubscriptionSubmission.from_dict(body)
    return web.Response(status=200)


async def subscriptions_id_delete(request: web.Request, id) -> web.Response:
    """Delete a subscription.

    

    :param id: Id of the subscription to delete
    :type id: str

    """
    return web.Response(status=200)
