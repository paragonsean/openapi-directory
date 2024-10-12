from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_payment_refund_response import GetPaymentRefundResponse
from openapi_server.models.list_payment_refunds_response import ListPaymentRefundsResponse
from openapi_server.models.refund_payment_request import RefundPaymentRequest
from openapi_server.models.refund_payment_response import RefundPaymentResponse
from openapi_server import util


async def get_payment_refund(request: web.Request, refund_id) -> web.Response:
    """GetPaymentRefund

    Retrieves a specific refund using the &#x60;refund_id&#x60;.

    :param refund_id: The unique ID for the desired &#x60;PaymentRefund&#x60;.
    :type refund_id: str

    """
    return web.Response(status=200)


async def list_payment_refunds(request: web.Request, begin_time=None, end_time=None, sort_order=None, cursor=None, location_id=None, status=None, source_type=None, limit=None) -> web.Response:
    """ListPaymentRefunds

    Retrieves a list of refunds for the account making the request.  Results are eventually consistent, and new refunds or changes to refunds might take several seconds to appear.  The maximum results per page is 100.

    :param begin_time: The timestamp for the beginning of the requested reporting period, in RFC 3339 format.  Default: The current time minus one year.
    :type begin_time: str
    :param end_time: The timestamp for the end of the requested reporting period, in RFC 3339 format.  Default: The current time.
    :type end_time: str
    :param sort_order: The order in which results are listed: - &#x60;ASC&#x60; - Oldest to newest. - &#x60;DESC&#x60; - Newest to oldest (default).
    :type sort_order: str
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    :type cursor: str
    :param location_id: Limit results to the location supplied. By default, results are returned for all locations associated with the seller.
    :type location_id: str
    :param status: If provided, only refunds with the given status are returned. For a list of refund status values, see [PaymentRefund](https://developer.squareup.com/reference/square_2021-08-18/objects/PaymentRefund).  Default: If omitted, refunds are returned regardless of their status.
    :type status: str
    :param source_type: If provided, only refunds with the given source type are returned. - &#x60;CARD&#x60; - List refunds only for payments where &#x60;CARD&#x60; was specified as the payment source.  Default: If omitted, refunds are returned regardless of the source type.
    :type source_type: str
    :param limit: The maximum number of results to be returned in a single page.  It is possible to receive fewer results than the specified limit on a given page.  If the supplied value is greater than 100, no more than 100 results are returned.  Default: 100
    :type limit: int

    """
    return web.Response(status=200)


async def refund_payment(request: web.Request, body) -> web.Response:
    """RefundPayment

    Refunds a payment. You can refund the entire payment amount or a portion of it. You can use this endpoint to refund a card payment or record a  refund of a cash or external payment. For more information, see [Refund Payment](https://developer.squareup.com/docs/payments-api/refund-payments).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = RefundPaymentRequest.from_dict(body)
    return web.Response(status=200)
