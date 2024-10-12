from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_check_request import BalanceCheckRequest
from openapi_server.models.balance_check_response import BalanceCheckResponse
from openapi_server.models.cancel_order_request import CancelOrderRequest
from openapi_server.models.cancel_order_response import CancelOrderResponse
from openapi_server.models.create_order_request import CreateOrderRequest
from openapi_server.models.create_order_response import CreateOrderResponse
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_orders(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Create an order

    Creates an order to be used for partial payments. Make a POST &#x60;/orders&#x60; call before making a &#x60;/payments&#x60; call when processing payments with different payment methods.

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrderRequest.from_dict(body)
    return web.Response(status=200)


async def post_orders_cancel(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Cancel an order

    Cancels an order. Cancellation of an order results in an automatic rollback of all payments made in the order, either by canceling or refunding the payment, depending on the type of payment method.

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = CancelOrderRequest.from_dict(body)
    return web.Response(status=200)


async def post_payment_methods_balance(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Get the balance of a gift card

    Retrieves the balance remaining on a shopper&#39;s gift card. To check a gift card&#39;s balance, make a POST &#x60;/paymentMethods/balance&#x60; call and include the gift card&#39;s details inside a &#x60;paymentMethod&#x60; object.

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = BalanceCheckRequest.from_dict(body)
    return web.Response(status=200)
