from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_request import SubscriptionRequest
from openapi_server.models.subscription_update import SubscriptionUpdate
from openapi_server import util


async def add_subscription(request: web.Request, body, x_anchore_account=None) -> web.Response:
    """Add a subscription of a specific type

    Create a new subscription to watch a tag and get notifications of changes

    :param body: 
    :type body: dict | bytes
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    body = SubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_subscription(request: web.Request, subscription_id, x_anchore_account=None) -> web.Response:
    """Delete subscriptions of a specific type

    

    :param subscription_id: 
    :type subscription_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def get_subscription(request: web.Request, subscription_id, x_anchore_account=None) -> web.Response:
    """Get a specific subscription set

    

    :param subscription_id: 
    :type subscription_id: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def list_subscriptions(request: web.Request, subscription_key=None, subscription_type=None, x_anchore_account=None) -> web.Response:
    """List all subscriptions

    

    :param subscription_key: filter only subscriptions matching key
    :type subscription_key: str
    :param subscription_type: filter only subscriptions matching type
    :type subscription_type: str
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)


async def update_subscription(request: web.Request, subscription_id, body, x_anchore_account=None) -> web.Response:
    """Update an existing and specific subscription

    

    :param subscription_id: 
    :type subscription_id: str
    :param body: 
    :type body: dict | bytes
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    body = SubscriptionUpdate.from_dict(body)
    return web.Response(status=200)
