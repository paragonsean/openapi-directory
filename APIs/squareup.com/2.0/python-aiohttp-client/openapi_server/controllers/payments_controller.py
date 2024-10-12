from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_payment_by_idempotency_key_request import CancelPaymentByIdempotencyKeyRequest
from openapi_server.models.cancel_payment_by_idempotency_key_response import CancelPaymentByIdempotencyKeyResponse
from openapi_server.models.cancel_payment_response import CancelPaymentResponse
from openapi_server.models.complete_payment_response import CompletePaymentResponse
from openapi_server.models.create_payment_request import CreatePaymentRequest
from openapi_server.models.create_payment_response import CreatePaymentResponse
from openapi_server.models.get_payment_response import GetPaymentResponse
from openapi_server.models.list_payments_response import ListPaymentsResponse
from openapi_server.models.update_payment_request import UpdatePaymentRequest
from openapi_server.models.update_payment_response import UpdatePaymentResponse
from openapi_server import util


async def cancel_payment(request: web.Request, payment_id) -> web.Response:
    """CancelPayment

    Cancels (voids) a payment. You can use this endpoint to cancel a payment with  the APPROVED &#x60;status&#x60;.

    :param payment_id: The ID of the payment to cancel.
    :type payment_id: str

    """
    return web.Response(status=200)


async def cancel_payment_by_idempotency_key(request: web.Request, body) -> web.Response:
    """CancelPaymentByIdempotencyKey

    Cancels (voids) a payment identified by the idempotency key that is specified in the request.  Use this method when the status of a &#x60;CreatePayment&#x60; request is unknown (for example, after you send a &#x60;CreatePayment&#x60; request, a network error occurs and you do not get a response). In this case, you can direct Square to cancel the payment using this endpoint. In the request, you provide the same idempotency key that you provided in your &#x60;CreatePayment&#x60; request that you want to cancel. After canceling the payment, you can submit your &#x60;CreatePayment&#x60; request again.  Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint returns successfully.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CancelPaymentByIdempotencyKeyRequest.from_dict(body)
    return web.Response(status=200)


async def complete_payment(request: web.Request, payment_id) -> web.Response:
    """CompletePayment

    Completes (captures) a payment. By default, payments are set to complete immediately after they are created.  You can use this endpoint to complete a payment with the APPROVED &#x60;status&#x60;.

    :param payment_id: The unique ID identifying the payment to be completed.
    :type payment_id: str

    """
    return web.Response(status=200)


async def create_payment(request: web.Request, body) -> web.Response:
    """CreatePayment

    Creates a payment using the provided source. You can use this endpoint  to charge a card (credit/debit card or     Square gift card) or record a payment that the seller received outside of Square  (cash payment from a buyer or a payment that an external entity  processed on behalf of the seller).  The endpoint creates a  &#x60;Payment&#x60; object and returns it in the response.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreatePaymentRequest.from_dict(body)
    return web.Response(status=200)


async def get_payment(request: web.Request, payment_id) -> web.Response:
    """GetPayment

    Retrieves details for a specific payment.

    :param payment_id: A unique ID for the desired payment.
    :type payment_id: str

    """
    return web.Response(status=200)


async def update_payment(request: web.Request, payment_id, body) -> web.Response:
    """UpdatePayment

    Updates a payment with the APPROVED status. You can update the &#x60;amount_money&#x60; and &#x60;tip_money&#x60; using this endpoint.

    :param payment_id: The ID of the payment to update.
    :type payment_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdatePaymentRequest.from_dict(body)
    return web.Response(status=200)


async def v2_payments_get(request: web.Request, begin_time=None, end_time=None, sort_order=None, cursor=None, location_id=None, total=None, last_4=None, card_brand=None, limit=None) -> web.Response:
    """ListPayments

    Retrieves a list of payments taken by the account making the request.  Results are eventually consistent, and new payments or changes to payments might take several seconds to appear.  The maximum results per page is 100.

    :param begin_time: The timestamp for the beginning of the reporting period, in RFC 3339 format. Inclusive. Default: The current time minus one year.
    :type begin_time: str
    :param end_time: The timestamp for the end of the reporting period, in RFC 3339 format.  Default: The current time.
    :type end_time: str
    :param sort_order: The order in which results are listed: - &#x60;ASC&#x60; - Oldest to newest. - &#x60;DESC&#x60; - Newest to oldest (default).
    :type sort_order: str
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    :type cursor: str
    :param location_id: Limit results to the location supplied. By default, results are returned for the default (main) location associated with the seller.
    :type location_id: str
    :param total: The exact amount in the &#x60;total_money&#x60; for a payment.
    :type total: int
    :param last_4: The last four digits of a payment card.
    :type last_4: str
    :param card_brand: The brand of the payment card (for example, VISA).
    :type card_brand: str
    :param limit: The maximum number of results to be returned in a single page. It is possible to receive fewer results than the specified limit on a given page.  The default value of 100 is also the maximum allowed value. If the provided value is  greater than 100, it is ignored and the default value is used instead.  Default: &#x60;100&#x60;
    :type limit: int

    """
    return web.Response(status=200)
