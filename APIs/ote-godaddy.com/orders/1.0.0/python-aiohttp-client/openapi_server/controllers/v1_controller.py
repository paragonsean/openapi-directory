from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit
from openapi_server.models.order import Order
from openapi_server.models.order_list import OrderList
from openapi_server import util


async def get(request: web.Request, order_id, x_shopper_id=None, x_market_id=None) -> web.Response:
    """Retrieve details for specified order

    &lt;strong&gt;API Resellers&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;This endpoint does not support subaccounts and therefore API Resellers should not supply an X-Shopper-Id header&lt;/li&gt;&lt;/ul&gt;

    :param order_id: Order id whose details are to be retrieved
    :type order_id: str
    :param x_shopper_id: Shopper ID to be operated on, if different from JWT&lt;br/&gt;&lt;b&gt;Reseller subaccounts are not supported&lt;/b&gt;
    :type x_shopper_id: str
    :param x_market_id: Unique identifier of the Market in which the request is happening
    :type x_market_id: str

    """
    return web.Response(status=200)


async def list(request: web.Request, period_start=None, period_end=None, domain=None, product_group_id=None, payment_profile_id=None, parent_order_id=None, offset=None, limit=None, sort=None, x_shopper_id=None, x_market_id=None) -> web.Response:
    """Retrieve a list of orders for the authenticated shopper. Only one filter may be used at a time

    &lt;strong&gt;API Resellers&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;This endpoint does not support subaccounts and therefore API Resellers should not supply an X-Shopper-Id header&lt;/li&gt;&lt;/ul&gt;

    :param period_start: Start of range indicating what time-frame should be returned. Inclusive
    :type period_start: str
    :param period_end: End of range indicating what time-frame should be returned. Inclusive
    :type period_end: str
    :param domain: Domain name to use as the filter of results
    :type domain: str
    :param product_group_id: Product group id to use as the filter of results
    :type product_group_id: int
    :param payment_profile_id: Payment profile id to use as the filter of results
    :type payment_profile_id: int
    :param parent_order_id: Parent order id to use as the filter of results
    :type parent_order_id: str
    :param offset: Number of results to skip for pagination
    :type offset: int
    :param limit: Maximum number of items to return
    :type limit: int
    :param sort: Property name that will be used to sort results. &#39;-&#39; indicates descending
    :type sort: str
    :param x_shopper_id: Shopper ID to be operated on, if different from JWT&lt;br/&gt;&lt;b&gt;Reseller subaccounts are not supported&lt;/b&gt;
    :type x_shopper_id: str
    :param x_market_id: Unique identifier of the Market in which the request is happening
    :type x_market_id: str

    """
    return web.Response(status=200)
