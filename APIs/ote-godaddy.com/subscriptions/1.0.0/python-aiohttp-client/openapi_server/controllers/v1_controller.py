from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.product_group import ProductGroup
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_list import SubscriptionList
from openapi_server.models.subscription_update import SubscriptionUpdate
from openapi_server import util


async def cancel(request: web.Request, subscription_id, x_shopper_id=None) -> web.Response:
    """Cancel the specified Subscription

    

    :param subscription_id: Unique identifier of the Subscription to cancel
    :type subscription_id: str
    :param x_shopper_id: Shopper ID to cancel subscriptions for when not using JWT
    :type x_shopper_id: str

    """
    return web.Response(status=200)


async def get(request: web.Request, subscription_id, x_shopper_id=None, x_market_id=None) -> web.Response:
    """Retrieve details for the specified Subscription

    

    :param subscription_id: Unique identifier of the Subscription to retrieve
    :type subscription_id: str
    :param x_shopper_id: Shopper ID to be operated on, if different from JWT
    :type x_shopper_id: str
    :param x_market_id: Unique identifier of the Market in which the request is happening
    :type x_market_id: str

    """
    return web.Response(status=200)


async def list(request: web.Request, x_shopper_id=None, x_market_id=None, product_group_keys=None, includes=None, offset=None, limit=None, sort=None) -> web.Response:
    """Retrieve a list of Subscriptions for the specified Shopper

    

    :param x_shopper_id: Shopper ID to return subscriptions for when not using JWT
    :type x_shopper_id: str
    :param x_market_id: The market that the response should be formatted for
    :type x_market_id: str
    :param product_group_keys: Only return Subscriptions with the specified product groups
    :type product_group_keys: List[str]
    :param includes: Optional details to be included in the response
    :type includes: List[str]
    :param offset: Number of Subscriptions to skip before starting to return paged results (must be a multiple of the limit)
    :type offset: int
    :param limit: Number of Subscriptions to retrieve in this page, starting after offset
    :type limit: int
    :param sort: Property name that will be used to sort results. \&quot;-\&quot; indicates descending
    :type sort: str

    """
    return web.Response(status=200)


async def product_groups(request: web.Request, x_shopper_id=None, x_market_id=None) -> web.Response:
    """Retrieve a list of ProductGroups for the specified Shopper

    

    :param x_shopper_id: Shopper ID to return data for when not using JWT
    :type x_shopper_id: str
    :param x_market_id: The market that the response should be formatted for
    :type x_market_id: str

    """
    return web.Response(status=200)


async def update(request: web.Request, subscription_id, body) -> web.Response:
    """Update details for the specified Subscription

    Only Subscription properties that can be changed without immediate financial impact can be modified via PATCH, whereas some properties can be changed by purchasing a renewal&lt;br/&gt;&lt;strong&gt;This endpoint only supports JWT authentication&lt;/strong&gt;

    :param subscription_id: Unique identifier of the Subscription to update
    :type subscription_id: str
    :param body: Details of the Subscription to change
    :type body: dict | bytes

    """
    body = SubscriptionUpdate.from_dict(body)
    return web.Response(status=200)
