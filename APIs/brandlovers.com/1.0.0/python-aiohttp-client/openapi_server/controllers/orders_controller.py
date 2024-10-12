from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_orders import GetOrders
from openapi_server.models.get_orders_shipments import GetOrdersShipments
from openapi_server.models.orders_shipments import OrdersShipments
from openapi_server import util


async def orders_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns orders details

    Retuns a list of orders associated with this seller. The list is ordered by dateCreated.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def orders_shipments_delivered_get(request: web.Request, authorization, status=None, offset=None, limit=None) -> web.Response:
    """Returns list of shipments

    Returns list of shipments. By default this will return list of the last shipments ordered by dateCreated, folowed by last update date.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param status: Query by shippment status.
    :type status: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def orders_shipments_delivered_post(request: web.Request, authorization, ordersshipments) -> web.Response:
    """Bulk update of order shipments

    Bulk update of order shipments status. This alows to inform multiple shipments status

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param ordersshipments: JSON body with list of shipments to be updated.
    :type ordersshipments: dict | bytes

    """
    ordersshipments = OrdersShipments.from_dict(ordersshipments)
    return web.Response(status=200)


async def orders_shipments_shipped_get(request: web.Request, authorization, status=None, offset=None, limit=None) -> web.Response:
    """Returns a list of shipments shipped

    Returns a list of shipments shipped. By Default returns items ordered by dateCreated folowed by last update

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param status: Product status.
    :type status: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def orders_shipments_shipped_post(request: web.Request, ordersshipments) -> web.Response:
    """Bulk update of order shipments

    Allows bulk updates of orders shippments.

    :param ordersshipments: JSON payload with list of shippments of orders.
    :type ordersshipments: dict | bytes

    """
    ordersshipments = OrdersShipments.from_dict(ordersshipments)
    return web.Response(status=200)


async def orders_status_approved_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Return list of approved orders

    Returns a list of approved orders. Orders in the &#x60;approved&#x60; state must be fullfiled imediadetelly.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 100, max 200. Use this in conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def orders_status_canceled_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns lists of canceled orders

    Returns a list with canceled orders. Canceled orders should not be fullfiled.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Default 100, max 250. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def orders_status_delivered_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns a list of orders successfully delivered associated with this seller.

    Returns a list of orders successfully delivered associated with this seller.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def orders_status_new_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns a list of orders flagged as new.

    Returns a list of orders flagged as new. New orders should not be fullfiled until marketplace flags them as approved.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def orders_status_partially_delivered_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns a list of partially deliverd orders

    Returns a list of partially deliverd orders. This is a list of orders with items shipped but with not all items ackwlodged as deliverd

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def orders_status_partially_sent_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns a list of orders partially fullfiled

    Returns a list of orders that contain one (or more) items that where not shipped. This will list the entire order as well the items with peding shipment. Use this service to track orders that need to be fullfiled.

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 100. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)


async def orders_status_sent_get(request: web.Request, authorization, offset=None, limit=None) -> web.Response:
    """Returns a list with orders fully sent

    Returns a list with orders completely fullfiled, this means orders with all items sent. Orders will ordered by dateCreated fowllowed by last update

    :param authorization: Authorization token. The Authorization token can be found in your Admin console.
    :type authorization: str
    :param offset: Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results.
    :type offset: int
    :param limit: Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results.
    :type limit: int

    """
    return web.Response(status=200)
