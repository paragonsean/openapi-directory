from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_retrieve_orders_request import BatchRetrieveOrdersRequest
from openapi_server.models.batch_retrieve_orders_response import BatchRetrieveOrdersResponse
from openapi_server.models.calculate_order_request import CalculateOrderRequest
from openapi_server.models.calculate_order_response import CalculateOrderResponse
from openapi_server.models.create_order_request import CreateOrderRequest
from openapi_server.models.create_order_response import CreateOrderResponse
from openapi_server.models.pay_order_request import PayOrderRequest
from openapi_server.models.pay_order_response import PayOrderResponse
from openapi_server.models.retrieve_order_response import RetrieveOrderResponse
from openapi_server.models.search_orders_request import SearchOrdersRequest
from openapi_server.models.search_orders_response import SearchOrdersResponse
from openapi_server.models.update_order_request import UpdateOrderRequest
from openapi_server.models.update_order_response import UpdateOrderResponse
from openapi_server import util


async def batch_retrieve_orders(request: web.Request, body) -> web.Response:
    """BatchRetrieveOrders

    Retrieves a set of [orders](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by their IDs.  If a given order ID does not exist, the ID is ignored instead of generating an error.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchRetrieveOrdersRequest.from_dict(body)
    return web.Response(status=200)


async def calculate_order(request: web.Request, body) -> web.Response:
    """CalculateOrder

    Enables applications to preview order pricing without creating an order.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CalculateOrderRequest.from_dict(body)
    return web.Response(status=200)


async def create_order(request: web.Request, body) -> web.Response:
    """CreateOrder

    Creates a new [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) that can include information about products for purchase and settings to apply to the purchase.  To pay for a created order, see  [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).  You can modify open orders using the [UpdateOrder](https://developer.squareup.com/reference/square_2021-08-18/orders-api/update-order) endpoint.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateOrderRequest.from_dict(body)
    return web.Response(status=200)


async def pay_order(request: web.Request, order_id, body) -> web.Response:
    """PayOrder

    Pay for an [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) using one or more approved [payments](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment) or settle an order with a total of &#x60;0&#x60;.  The total of the &#x60;payment_ids&#x60; listed in the request must be equal to the order total. Orders with a total amount of &#x60;0&#x60; can be marked as paid by specifying an empty array of &#x60;payment_ids&#x60; in the request.  To be used with &#x60;PayOrder&#x60;, a payment must:  - Reference the order by specifying the &#x60;order_id&#x60; when [creating the payment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/create-payment). Any approved payments that reference the same &#x60;order_id&#x60; not specified in the &#x60;payment_ids&#x60; is canceled. - Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments#delayed-capture). Using a delayed capture payment with &#x60;PayOrder&#x60; completes the approved payment.

    :param order_id: The ID of the order being paid.
    :type order_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = PayOrderRequest.from_dict(body)
    return web.Response(status=200)


async def search_orders(request: web.Request, body) -> web.Response:
    """SearchOrders

    Search all orders for one or more locations. Orders include all sales, returns, and exchanges regardless of how or when they entered the Square ecosystem (such as Point of Sale, Invoices, and Connect APIs).  &#x60;SearchOrders&#x60; requests need to specify which locations to search and define a [SearchOrdersQuery](https://developer.squareup.com/reference/square_2021-08-18/objects/SearchOrdersQuery) object that controls how to sort or filter the results. Your &#x60;SearchOrdersQuery&#x60; can:    Set filter criteria.   Set the sort order.   Determine whether to return results as complete &#x60;Order&#x60; objects or as [OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects.  Note that details for orders processed with Square Point of Sale while in offline mode might not be transmitted to Square for up to 72 hours. Offline orders have a &#x60;created_at&#x60; value that reflects the time the order was created, not the time it was subsequently transmitted to Square.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchOrdersRequest.from_dict(body)
    return web.Response(status=200)


async def v2_orders_order_id_get(request: web.Request, order_id) -> web.Response:
    """RetrieveOrder

    Retrieves an [Order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by ID.

    :param order_id: The ID of the order to retrieve.
    :type order_id: str

    """
    return web.Response(status=200)


async def v2_orders_order_id_put(request: web.Request, order_id, body) -> web.Response:
    """UpdateOrder

    Updates an open [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) by adding, replacing, or deleting fields. Orders with a &#x60;COMPLETED&#x60; or &#x60;CANCELED&#x60; state cannot be updated.  An &#x60;UpdateOrder&#x60; request requires the following:  - The &#x60;order_id&#x60; in the endpoint path, identifying the order to update. - The latest &#x60;version&#x60; of the order to update. - The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders#sparse-order-objects) containing only the fields to update and the version to which the update is being applied. - If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders#on-dot-notation) identifying the fields to clear.  To pay for an order, see  [Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

    :param order_id: The ID of the order to update.
    :type order_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateOrderRequest.from_dict(body)
    return web.Response(status=200)
