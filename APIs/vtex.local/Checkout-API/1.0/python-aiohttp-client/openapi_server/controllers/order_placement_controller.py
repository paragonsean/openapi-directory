from typing import List, Dict
from aiohttp import web

from openapi_server.models.place_order200_response import PlaceOrder200Response
from openapi_server.models.place_order_from_existing_order_form_request import PlaceOrderFromExistingOrderFormRequest
from openapi_server.models.place_order_request import PlaceOrderRequest
from openapi_server.models.process_order500_response import ProcessOrder500Response
from openapi_server import util


async def place_order(request: web.Request, content_type, accept, sc=None, body=None) -> web.Response:
    """Place order

    Places order without having any prior cart information. This means all information on items, client, payment and shipping must be sent in the body.    &gt;⚠️ The authentication of this endpoint is required if you are creating an order with an item that has an attachment that creates a Subscription. For more information, access [Subscriptions API](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sc: Trade Policy (Sales Channel) identification. This query can be used to create an order for a specific sales channel.
    :type sc: int
    :param body: 
    :type body: dict | bytes

    """
    body = PlaceOrderRequest.from_dict(body)
    return web.Response(status=200)


async def place_order_from_existing_order_form(request: web.Request, order_form_id, content_type, accept, body=None) -> web.Response:
    """Place order from an existing cart

    This endpoint places an order from an existing &#x60;orderForm&#x60; object, meaning an existing cart.    After the creation of an order with this request, you have five minutes to send payment information and then request payment processing.

    :param order_form_id: ID of the &#x60;orderForm&#x60; corresponding to the cart from which to place the order.
    :type order_form_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlaceOrderFromExistingOrderFormRequest.from_dict(body)
    return web.Response(status=200)


async def process_order(request: web.Request, order_group, content_type, accept, cookie) -> web.Response:
    """Process order

    Order processing callback request, which is made after an order&#39;s payment is approved.    &gt; This request has to be made until five minutes after the [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders) or [Place order from existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) request has been made, or else, the order will not be processed.

    :param order_group: Order group. It is the part of the &#x60;orderId&#x60; that comes before the &#x60;-&#x60;. For example, the &#x60;orderGroup&#x60; of the order &#x60;123456789-01&#x60; is &#x60;123456789&#x60;.
    :type order_group: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param cookie: VTEX Chekout cookie associated with a specific order. Use the &#x60;Vtex_CHKO_Auth&#x60; and the &#x60;CheckoutDataAccess&#x60; cookies returned by the [Place order](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorder) or [Place order from existing cart](https://developers.vtex.com/vtex-rest-api/reference/order-placement-1#placeorderfromexistingorderform) API requests, like a browser would.
    :type cookie: str

    """
    return web.Response(status=200)
