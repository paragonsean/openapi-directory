from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_request3d import PaymentRequest3d
from openapi_server.models.payment_request3ds2 import PaymentRequest3ds2
from openapi_server.models.payment_result import PaymentResult
from openapi_server.models.service_error import ServiceError
from openapi_server.models.three_ds2_result_request import ThreeDS2ResultRequest
from openapi_server.models.three_ds2_result_response import ThreeDS2ResultResponse
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


async def post_authorise3ds2(request: web.Request, body=None) -> web.Response:
    """Complete a 3DS2 authorisation

    For an authenticated 3D Secure 2 session, completes the payment authorisation. This endpoint must receive the &#x60;threeDS2Token&#x60; and &#x60;threeDS2Result&#x60; parameters.  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce/3d-secure). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/details&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/details) endpoint under Checkout API instead.

    :param body: 
    :type body: dict | bytes

    """
    body = PaymentRequest3ds2.from_dict(body)
    return web.Response(status=200)


async def post_retrieve3ds2_result(request: web.Request, body=None) -> web.Response:
    """Get the 3DS2 authentication result

    Retrieves the &#x60;threeDS2Result&#x60; after doing a 3D Secure 2 authentication only.

    :param body: 
    :type body: dict | bytes

    """
    body = ThreeDS2ResultRequest.from_dict(body)
    return web.Response(status=200)
