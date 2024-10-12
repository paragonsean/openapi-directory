from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_setup_request import PaymentSetupRequest
from openapi_server.models.payment_setup_response import PaymentSetupResponse
from openapi_server.models.payment_verification_request import PaymentVerificationRequest
from openapi_server.models.payment_verification_response import PaymentVerificationResponse
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_payment_session(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Create a payment session

    Provides the data object that can be used to start the Checkout SDK. To set up the payment, pass its amount, currency, and other required parameters. We use this to optimise the payment flow and perform better risk assessment of the transaction.  For more information, refer to [How it works](https://docs.adyen.com/online-payments#howitworks).

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentSetupRequest.from_dict(body)
    return web.Response(status=200)


async def post_payments_result(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Verify a payment result

    Verifies the payment result using the payload returned from the Checkout SDK.  For more information, refer to [How it works](https://docs.adyen.com/online-payments#howitworks).

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentVerificationRequest.from_dict(body)
    return web.Response(status=200)
