from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription import Subscription
from openapi_server import util


async def maps_id_subscriptions_delete(request: web.Request, id) -> web.Response:
    """Unsubscribe from map

    Unsubscribe from map.

    :param id: map id
    :type id: int

    """
    return web.Response(status=200)


async def maps_id_subscriptions_get(request: web.Request, id) -> web.Response:
    """List subscriptions for a given map

    List subscriptions for a given map.

    :param id: Id of map
    :type id: int

    """
    return web.Response(status=200)


async def subscriptions_get(request: web.Request, user_id=None, map_id=None) -> web.Response:
    """List subscriptions. Pass no parameters to get own subscriptions

    List subscriptions.

    :param user_id: Id of user
    :type user_id: int
    :param map_id: Id of map
    :type map_id: int

    """
    return web.Response(status=200)


async def subscriptions_post(request: web.Request, map_id) -> web.Response:
    """Create map subscription

    Create map subscription.

    :param map_id: map id
    :type map_id: 

    """
    return web.Response(status=200)
