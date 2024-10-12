from typing import List, Dict
from aiohttp import web

from openapi_server.models.card_details_request import CardDetailsRequest
from openapi_server.models.card_details_response import CardDetailsResponse
from openapi_server.models.create_checkout_session_request import CreateCheckoutSessionRequest
from openapi_server.models.create_checkout_session_response import CreateCheckoutSessionResponse
from openapi_server.models.payment_details_request import PaymentDetailsRequest
from openapi_server.models.payment_details_response import PaymentDetailsResponse
from openapi_server.models.payment_methods_request import PaymentMethodsRequest
from openapi_server.models.payment_methods_response import PaymentMethodsResponse
from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_response import PaymentResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.session_result_response import SessionResultResponse
from openapi_server import util


async def get_sessions_session_id(request: web.Request, session_id, session_result) -> web.Response:
    """Get the result of a payment session

    Returns the status of the payment session with the &#x60;sessionId&#x60; and &#x60;sessionResult&#x60; specified in the path.

    :param session_id: A unique identifier of the session.
    :type session_id: str
    :param session_result: The &#x60;sessionResult&#x60; value from the Drop-in or Component.
    :type session_result: str

    """
    return web.Response(status=200)


async def post_card_details(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Get the list of brands on the card

    Send a request with at least the first 6 digits of the card number to get a response with an array of brands on the card. If you include [your supported brands](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cardDetails__reqParam_supportedBrands) in the request, the response also tells you if you support each [brand that was identified](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cardDetails__resParam_details).  If you have an API-only integration and collect card data, use this endpoint to find out if the shopper&#39;s card is co-branded. For co-branded cards, you must let the shopper choose the brand to pay with  if you support both brands.  

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = CardDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def post_payment_methods(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Get a list of available payment methods

    Queries the available payment methods for a transaction based on the transaction context (like amount, country, and currency). Besides giving back a list of the available payment methods, the response also returns which input details you need to collect from the shopper (to be submitted to &#x60;/payments&#x60;).  Although we highly recommend using this endpoint to ensure you are always offering the most up-to-date list of payment methods, its usage is optional. You can, for example, also cache the &#x60;/paymentMethods&#x60; response and update it once a week.

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentMethodsRequest.from_dict(body)
    return web.Response(status=200)


async def post_payments(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Start a transaction

    Sends payment parameters (like amount, country, and currency) together with other required input details collected from the shopper. To know more about required parameters for specific payment methods, refer to our [payment method guides](https://docs.adyen.com/payment-methods).  The response depends on the [payment flow](https://docs.adyen.com/payment-methods#payment-flow): * For a direct flow, the response includes a &#x60;pspReference&#x60; and a &#x60;resultCode&#x60; with the payment result, for example **Authorised** or **Refused**.  * For a redirect or additional action, the response contains an &#x60;action&#x60; object. 

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentRequest.from_dict(body)
    return web.Response(status=200)


async def post_payments_details(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Submit details for a payment

    Submits details for a payment created using &#x60;/payments&#x60;. This step is only needed when no final state has been reached on the &#x60;/payments&#x60; request, for example when the shopper was redirected to another page to complete the payment.  

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def post_sessions(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Create a payment session

    Creates a payment session for [Web Drop-in](https://docs.adyen.com/online-payments/web-drop-in) and [Web Components](https://docs.adyen.com/online-payments/web-components) integrations.  The response contains encrypted payment session data. The front end then uses the session data to make any required server-side calls for the payment flow.  You get the payment outcome asynchronously, in an [AUTHORISATION](https://docs.adyen.com/api-explorer/#/Webhooks/latest/post/AUTHORISATION) webhook.

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCheckoutSessionRequest.from_dict(body)
    return web.Response(status=200)
