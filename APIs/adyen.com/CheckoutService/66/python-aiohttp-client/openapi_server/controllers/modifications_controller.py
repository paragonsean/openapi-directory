from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_amount_update_request import PaymentAmountUpdateRequest
from openapi_server.models.payment_amount_update_response import PaymentAmountUpdateResponse
from openapi_server.models.payment_cancel_request import PaymentCancelRequest
from openapi_server.models.payment_cancel_response import PaymentCancelResponse
from openapi_server.models.payment_capture_request import PaymentCaptureRequest
from openapi_server.models.payment_capture_response import PaymentCaptureResponse
from openapi_server.models.payment_refund_request import PaymentRefundRequest
from openapi_server.models.payment_refund_response import PaymentRefundResponse
from openapi_server.models.payment_reversal_request import PaymentReversalRequest
from openapi_server.models.payment_reversal_response import PaymentReversalResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.standalone_payment_cancel_request import StandalonePaymentCancelRequest
from openapi_server.models.standalone_payment_cancel_response import StandalonePaymentCancelResponse
from openapi_server import util


async def post_cancels(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Cancel an authorised payment

    Cancels the authorisation on a payment that has not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**TECHNICAL_CANCEL** webhook](https://docs.adyen.com/online-payments/cancel#cancellation-webhook).  If you want to cancel a payment using the [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference), use the [&#x60;/payments/{paymentPspReference}/cancels&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels) endpoint instead.  If you want to cancel a payment but are not sure whether it has been captured, use the [&#x60;/payments/{paymentPspReference}/reversals&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals) endpoint instead.  For more information, refer to [Cancel](https://docs.adyen.com/online-payments/cancel).

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = StandalonePaymentCancelRequest.from_dict(body)
    return web.Response(status=200)


async def post_payments_payment_psp_reference_amount_updates(request: web.Request, payment_psp_reference, idempotency_key=None, body=None) -> web.Response:
    """Update an authorised amount

    Increases or decreases the authorised payment amount and returns a unique reference for this request. You get the outcome of the request asynchronously, in an [**AUTHORISATION_ADJUSTMENT** webhook](https://docs.adyen.com/development-resources/webhooks/understand-notifications#event-codes).  You can only update authorised amounts that have not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures).  The amount you specify in the request is the updated amount, which is larger or smaller than the initial authorised amount.  For more information, refer to [Authorisation adjustment](https://docs.adyen.com/online-payments/adjust-authorisation#use-cases).

    :param payment_psp_reference: The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment.
    :type payment_psp_reference: str
    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentAmountUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def post_payments_payment_psp_reference_cancels(request: web.Request, payment_psp_reference, idempotency_key=None, body=None) -> web.Response:
    """Cancel an authorised payment

    Cancels the authorisation on a payment that has not yet been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/paymentPspReference/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CANCELLATION** webhook](https://docs.adyen.com/online-payments/cancel#cancellation-webhook).  If you want to cancel a payment but don&#39;t have the [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference), use the [&#x60;/cancels&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/cancels) endpoint instead.  If you want to cancel a payment but are not sure whether it has been captured, use the [&#x60;/payments/{paymentPspReference}/reversals&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals) endpoint instead.  For more information, refer to [Cancel](https://docs.adyen.com/online-payments/cancel).

    :param payment_psp_reference: The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to cancel. 
    :type payment_psp_reference: str
    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentCancelRequest.from_dict(body)
    return web.Response(status=200)


async def post_payments_payment_psp_reference_captures(request: web.Request, payment_psp_reference, idempotency_key=None, body=None) -> web.Response:
    """Capture an authorised payment

     Captures an authorised payment and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CAPTURE** webhook](https://docs.adyen.com/online-payments/capture#capture-notification).  You can capture either the full authorised amount or a part of the authorised amount. By default, any unclaimed amount after a partial capture gets cancelled. This does not apply if you enabled multiple partial captures on your account and the payment method supports multiple partial captures.   [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture) is the default setting for most payment methods. In these cases, you don&#39;t need to make capture requests. However, making capture requests for payments that are captured automatically does not result in double charges.  For more information, refer to [Capture](https://docs.adyen.com/online-payments/capture).

    :param payment_psp_reference: The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to capture.
    :type payment_psp_reference: str
    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentCaptureRequest.from_dict(body)
    return web.Response(status=200)


async def post_payments_payment_psp_reference_refunds(request: web.Request, payment_psp_reference, idempotency_key=None, body=None) -> web.Response:
    """Refund a captured payment

    Refunds a payment that has been [captured](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/captures), and returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**REFUND** webhook](https://docs.adyen.com/online-payments/refund#refund-webhook).  You can refund either the full captured amount or a part of the captured amount. You can also perform multiple partial refunds, as long as their sum doesn&#39;t exceed the captured amount.  &gt; Some payment methods do not support partial refunds. To learn if a payment method supports partial refunds, refer to the payment method page such as [cards](https://docs.adyen.com/payment-methods/cards#supported-cards), [iDEAL](https://docs.adyen.com/payment-methods/ideal), or [Klarna](https://docs.adyen.com/payment-methods/klarna).   If you want to refund a payment but are not sure whether it has been captured, use the [&#x60;/payments/{paymentPspReference}/reversals&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/reversals) endpoint instead.  For more information, refer to [Refund](https://docs.adyen.com/online-payments/refund).

    :param payment_psp_reference: The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to refund.
    :type payment_psp_reference: str
    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentRefundRequest.from_dict(body)
    return web.Response(status=200)


async def post_payments_payment_psp_reference_reversals(request: web.Request, payment_psp_reference, idempotency_key=None, body=None) -> web.Response:
    """Refund or cancel a payment

    [Refunds](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/refunds) a payment if it has already been captured, and [cancels](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments/{paymentPspReference}/cancels) a payment if it has not yet been captured. Returns a unique reference for this request. You get the outcome of the request asynchronously, in a [**CANCEL_OR_REFUND** webhook](https://docs.adyen.com/online-payments/reverse#cancel-or-refund-webhook).  The reversed amount is always the full payment amount. &gt; Do not use this request for payments that involve multiple partial captures.  For more information, refer to [Reversal](https://docs.adyen.com/online-payments/reversal).

    :param payment_psp_reference: The [&#x60;pspReference&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_pspReference) of the payment that you want to reverse. 
    :type payment_psp_reference: str
    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentReversalRequest.from_dict(body)
    return web.Response(status=200)
