from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_request3d import PaymentRequest3d
from openapi_server.models.payment_result import PaymentResult
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_authorise(request: web.Request, body=None) -> web.Response:
    """Create an authorisation

    Creates a payment with a unique reference (&#x60;pspReference&#x60;) and attempts to obtain an authorisation hold. For cards, this amount can be captured or cancelled later. Non-card payment methods typically don&#39;t support this and will automatically capture as part of the authorisation. &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments) endpoint under Checkout API instead.

    :param body: 
    :type body: dict | bytes

    """
    body = PaymentRequest.from_dict(body)
    return web.Response(status=200)


async def post_authorise3d(request: web.Request, body=None) -> web.Response:
    """Complete a 3DS authorisation

    For an authenticated 3D Secure session, completes the payment authorisation. This endpoint must receive the &#x60;md&#x60; and &#x60;paResponse&#x60; parameters that you get from the card issuer after a shopper pays via 3D Secure.  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce/3d-secure). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/details&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/details) endpoint under Checkout API instead.

    :param body: 
    :type body: dict | bytes

    """
    body = PaymentRequest3d.from_dict(body)
    return web.Response(status=200)
