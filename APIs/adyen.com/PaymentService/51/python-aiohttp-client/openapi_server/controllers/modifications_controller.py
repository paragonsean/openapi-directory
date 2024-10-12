from typing import List, Dict
from aiohttp import web

from openapi_server.models.adjust_authorisation_request import AdjustAuthorisationRequest
from openapi_server.models.cancel_or_refund_request import CancelOrRefundRequest
from openapi_server.models.cancel_request import CancelRequest
from openapi_server.models.capture_request import CaptureRequest
from openapi_server.models.donation_request import DonationRequest
from openapi_server.models.modification_result import ModificationResult
from openapi_server.models.refund_request import RefundRequest
from openapi_server.models.service_error import ServiceError
from openapi_server.models.technical_cancel_request import TechnicalCancelRequest
from openapi_server.models.void_pending_refund_request import VoidPendingRefundRequest
from openapi_server import util


async def post_adjust_authorisation(request: web.Request, body=None) -> web.Response:
    """Change the authorised amount

    Allows you to increase or decrease the authorised amount after the initial authorisation has taken place. This functionality enables for example tipping, improving the chances your authorisation will be valid, or charging the shopper when they have already left the merchant premises.  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). &gt; If you have a [newer integration](https://docs.adyen.com/online-payments), and are doing: &gt; * [Asynchronous adjustments](https://docs.adyen.com/online-payments/adjust-authorisation#asynchronous-or-synchronous-adjustment), use the [&#x60;/payments/{paymentPspReference}/amountUpdates&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/v67/post/payments/{paymentPspReference}/amountUpdates) endpoint on Checkout API. &gt; * [Synchronous adjustments](https://docs.adyen.com/online-payments/adjust-authorisation#asynchronous-or-synchronous-adjustment), use this endpoint.

    :param body: 
    :type body: dict | bytes

    """
    body = AdjustAuthorisationRequest.from_dict(body)
    return web.Response(status=200)


async def post_cancel(request: web.Request, body=None) -> web.Response:
    """Cancel an authorisation

    Cancels the authorisation hold on a payment, returning a unique reference for this request. You can cancel payments after authorisation only for payment methods that support distinct authorisations and captures.  For more information, refer to [Cancel](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel).  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/{paymentPspReference}/cancels&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/{paymentPspReference}/cancels) endpoint under Checkout API instead.

    :param body: 
    :type body: dict | bytes

    """
    body = CancelRequest.from_dict(body)
    return web.Response(status=200)


async def post_cancel_or_refund(request: web.Request, body=None) -> web.Response:
    """Cancel or refund a payment

    Cancels a payment if it has not been captured yet, or refunds it if it has already been captured. This is useful when it is not certain if the payment has been captured or not (for example, when using auto-capture).  Do not use this endpoint for payments that involve:  * [Multiple partial captures](https://docs.adyen.com/online-payments/capture).  * [Split data](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information) either at time of payment or capture for Adyen for Platforms.   Instead, check if the payment has been captured and make a corresponding [&#x60;/refund&#x60;](https://docs.adyen.com/api-explorer/#/Payment/refund) or [&#x60;/cancel&#x60;](https://docs.adyen.com/api-explorer/#/Payment/cancel) call.  For more information, refer to [Cancel or refund](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel-or-refund).  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/{paymentPspReference}/reversals&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/{paymentPspReference}/reversals) endpoint under Checkout API instead.

    :param body: 
    :type body: dict | bytes

    """
    body = CancelOrRefundRequest.from_dict(body)
    return web.Response(status=200)


async def post_capture(request: web.Request, body=None) -> web.Response:
    """Capture an authorisation

    Captures the authorisation hold on a payment, returning a unique reference for this request. Usually the full authorisation amount is captured, however it&#39;s also possible to capture a smaller amount, which results in cancelling the remaining authorisation balance.  Payment methods that are captured automatically after authorisation don&#39;t need to be captured. However, submitting a capture request on these transactions will not result in double charges. If immediate or delayed auto-capture is enabled, calling the capture method is not neccessary.  For more information refer to [Capture](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/capture).  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/{paymentPspReference}/captures&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/v67/post/payments/{paymentPspReference}/captures) endpoint on Checkout API instead.  

    :param body: 
    :type body: dict | bytes

    """
    body = CaptureRequest.from_dict(body)
    return web.Response(status=200)


async def post_donate(request: web.Request, body=None) -> web.Response:
    """Create a donation

    Schedules a new payment to be created (including a new authorisation request) for the specified donation using the payment details of the original payment.  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/donations&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/donations) endpoint under Checkout API instead.

    :param body: 
    :type body: dict | bytes

    """
    body = DonationRequest.from_dict(body)
    return web.Response(status=200)


async def post_refund(request: web.Request, body=None) -> web.Response:
    """Refund a captured payment

    Refunds a payment that has previously been captured, returning a unique reference for this request. Refunding can be done on the full captured amount or a partial amount. Multiple (partial) refunds will be accepted as long as their sum doesn&#39;t exceed the captured amount. Payments which have been authorised, but not captured, cannot be refunded, use the /cancel method instead.  Some payment methods/gateways do not support partial/multiple refunds. A margin above the captured limit can be configured to cover shipping/handling costs.  For more information, refer to [Refund](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/refund).  &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/payments/{paymentPspReference}/refunds&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/payments/{paymentPspReference}/refunds) endpoint under Checkout API instead.

    :param body: 
    :type body: dict | bytes

    """
    body = RefundRequest.from_dict(body)
    return web.Response(status=200)


async def post_technical_cancel(request: web.Request, body=None) -> web.Response:
    """Cancel an authorisation using your reference

    This endpoint allows you to cancel a payment if you do not have the PSP reference of the original payment request available.  In your call, refer to the original payment by using the &#x60;reference&#x60; that you specified in your payment request.  For more information, see [Technical cancel](https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel#technical-cancel).   &gt; This endpoint is part of our [classic API integration](https://docs.adyen.com/online-payments/classic-integrations/api-integration-ecommerce). If using a [newer integration](https://docs.adyen.com/online-payments), use the [&#x60;/cancels&#x60;](https://docs.adyen.com/api-explorer/#/CheckoutService/cancels) endpoint under Checkout API instead.

    :param body: 
    :type body: dict | bytes

    """
    body = TechnicalCancelRequest.from_dict(body)
    return web.Response(status=200)


async def post_void_pending_refund(request: web.Request, body=None) -> web.Response:
    """Cancel an in-person refund

    This endpoint allows you to cancel an unreferenced refund request before it has been completed.  In your call, you can refer to the original refund request either by using the &#x60;tenderReference&#x60;, or the &#x60;pspReference&#x60;. We recommend implementing based on the &#x60;tenderReference&#x60;, as this is generated for both offline and online transactions.  For more information, refer to [Cancel an unreferenced refund](https://docs.adyen.com/point-of-sale/refund-payment/cancel-unreferenced).

    :param body: 
    :type body: dict | bytes

    """
    body = VoidPendingRefundRequest.from_dict(body)
    return web.Response(status=200)
