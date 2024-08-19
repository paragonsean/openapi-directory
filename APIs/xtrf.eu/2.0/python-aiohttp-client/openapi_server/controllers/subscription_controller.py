from typing import List, Dict
from aiohttp import web

from openapi_server.models.active_subscription_dto import ActiveSubscriptionDTO
from openapi_server.models.subscription_dto import SubscriptionDTO
from openapi_server import util


async def are_hooks_supported(request: web.Request, ) -> web.Response:
    """This method can be used to determine if hooks are supported.

    This method can be used to determine if hooks are supported.


    """
    return web.Response(status=200)


async def get_all4(request: web.Request, ) -> web.Response:
    """Returns all subscriptions

    Returns all subscriptions. Subscriptions are automatically removed if they do not work (ie. if 404 status is returned). To improve notification reliability one can use this method to check if subscription is still active and re-subscribe if necessary.


    """
    return web.Response(status=200)


async def subscribe(request: web.Request, body) -> web.Response:
    """Subscribe to event

    Subscribe to event. Returns subscription Id.

    :param body: Returns subscription Id.
    :type body: dict | bytes

    """
    body = SubscriptionDTO.from_dict(body)
    return web.Response(status=200)


async def unsubscribe(request: web.Request, subscription_id) -> web.Response:
    """Unsubscribe from event

    Unsubscribe from job status changed event

    :param subscription_id: 
    :type subscription_id: str

    """
    return web.Response(status=200)
