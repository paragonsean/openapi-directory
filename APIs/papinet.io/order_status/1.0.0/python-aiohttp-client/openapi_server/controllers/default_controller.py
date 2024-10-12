from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_of_orders import ListOfOrders
from openapi_server.models.order import Order
from openapi_server import util


async def orders_get(request: web.Request, order_status=None, offset=None, limit=None) -> web.Response:
    """List &#x60;orders&#x60;

    Gets a paginated list of all &#x60;orders&#x60;.

    :param order_status: Filter by status
    :type order_status: str
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: str
    :param limit: The maximum number of items to return. If the value exceeds the maximum, then the maximum value will be used.
    :type limit: str

    """
    return web.Response(status=200)


async def orders_order_id_get(request: web.Request, order_id) -> web.Response:
    """Get an &#x60;order&#x60;

    Gets the details of a specific &#x60;order&#x60;, including a paginated list of all its lines.

    :param order_id: UUID of the &#x60;order&#x60; to get
    :type order_id: str
    :type order_id: str

    """
    return web.Response(status=200)
