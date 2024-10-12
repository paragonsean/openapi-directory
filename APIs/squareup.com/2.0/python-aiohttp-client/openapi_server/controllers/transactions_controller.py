from typing import List, Dict
from aiohttp import web

from openapi_server.models.capture_transaction_response import CaptureTransactionResponse
from openapi_server.models.charge_request import ChargeRequest
from openapi_server.models.charge_response import ChargeResponse
from openapi_server.models.create_refund_request import CreateRefundRequest
from openapi_server.models.create_refund_response import CreateRefundResponse
from openapi_server.models.list_refunds_response import ListRefundsResponse
from openapi_server.models.list_transactions_response import ListTransactionsResponse
from openapi_server.models.retrieve_transaction_response import RetrieveTransactionResponse
from openapi_server.models.void_transaction_response import VoidTransactionResponse
from openapi_server import util


async def capture_transaction(request: web.Request, location_id, transaction_id) -> web.Response:
    """CaptureTransaction

    Captures a transaction that was created with the [Charge](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/charge) endpoint with a &#x60;delay_capture&#x60; value of &#x60;true&#x60;.   See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture) for more information.

    :param location_id: 
    :type location_id: str
    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)


async def charge(request: web.Request, location_id, body) -> web.Response:
    """Charge

    Charges a card represented by a card nonce or a customer&#39;s card on file.  Your request to this endpoint must include _either_:  - A value for the &#x60;card_nonce&#x60; parameter (to charge a card payment token generated with the Web Payments SDK) - Values for the &#x60;customer_card_id&#x60; and &#x60;customer_id&#x60; parameters (to charge a customer&#39;s card on file)  In order for an eCommerce payment to potentially qualify for [Square chargeback protection](https://squareup.com/help/article/5394), you _must_ provide values for the following parameters in your request:  - &#x60;buyer_email_address&#x60; - At least one of &#x60;billing_address&#x60; or &#x60;shipping_address&#x60;  When this response is returned, the amount of Square&#39;s processing fee might not yet be calculated. To obtain the processing fee, wait about ten seconds and call [RetrieveTransaction](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/retrieve-transaction). See the &#x60;processing_fee_money&#x60; field of each [Tender included](https://developer.squareup.com/reference/square_2021-08-18/objects/Tender) in the transaction.

    :param location_id: The ID of the location to associate the created transaction with.
    :type location_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = ChargeRequest.from_dict(body)
    return web.Response(status=200)


async def list_transactions(request: web.Request, location_id, begin_time=None, end_time=None, sort_order=None, cursor=None) -> web.Response:
    """ListTransactions

    Lists transactions for a particular location.  Transactions include payment information from sales and exchanges and refund information from returns and exchanges.  Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

    :param location_id: The ID of the location to list transactions for.
    :type location_id: str
    :param begin_time: The beginning of the requested reporting period, in RFC 3339 format.  See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.  Default value: The current time minus one year.
    :type begin_time: str
    :param end_time: The end of the requested reporting period, in RFC 3339 format.  See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.  Default value: The current time.
    :type end_time: str
    :param sort_order: The order in which results are listed in the response (&#x60;ASC&#x60; for oldest first, &#x60;DESC&#x60; for newest first).  Default value: &#x60;DESC&#x60;
    :type sort_order: str
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    :type cursor: str

    """
    return web.Response(status=200)


async def retrieve_transaction(request: web.Request, location_id, transaction_id) -> web.Response:
    """RetrieveTransaction

    Retrieves details for a single transaction.

    :param location_id: The ID of the transaction&#39;s associated location.
    :type location_id: str
    :param transaction_id: The ID of the transaction to retrieve.
    :type transaction_id: str

    """
    return web.Response(status=200)


async def v2_locations_location_id_refunds_get(request: web.Request, location_id, begin_time=None, end_time=None, sort_order=None, cursor=None) -> web.Response:
    """ListRefunds

    Lists refunds for one of a business&#39;s locations.  In addition to full or partial tender refunds processed through Square APIs, refunds may result from itemized returns or exchanges through Square&#39;s Point of Sale applications.  Refunds with a &#x60;status&#x60; of &#x60;PENDING&#x60; are not currently included in this endpoint&#39;s response.  Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

    :param location_id: The ID of the location to list refunds for.
    :type location_id: str
    :param begin_time: The beginning of the requested reporting period, in RFC 3339 format.  See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.  Default value: The current time minus one year.
    :type begin_time: str
    :param end_time: The end of the requested reporting period, in RFC 3339 format.  See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.  Default value: The current time.
    :type end_time: str
    :param sort_order: The order in which results are listed in the response (&#x60;ASC&#x60; for oldest first, &#x60;DESC&#x60; for newest first).  Default value: &#x60;DESC&#x60;
    :type sort_order: str
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    :type cursor: str

    """
    return web.Response(status=200)


async def v2_locations_location_id_transactions_transaction_id_refund_post(request: web.Request, location_id, transaction_id, body) -> web.Response:
    """CreateRefund

    Initiates a refund for a previously charged tender.  You must issue a refund within 120 days of the associated payment. See [this article](https://squareup.com/help/us/en/article/5060) for more information on refund behavior.  NOTE: Card-present transactions with Interac credit cards **cannot be refunded using the Connect API**. Interac transactions must refunded in-person (e.g., dipping the card using POS app).

    :param location_id: The ID of the original transaction&#39;s associated location.
    :type location_id: str
    :param transaction_id: The ID of the original transaction that includes the tender to refund.
    :type transaction_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateRefundRequest.from_dict(body)
    return web.Response(status=200)


async def void_transaction(request: web.Request, location_id, transaction_id) -> web.Response:
    """VoidTransaction

    Cancels a transaction that was created with the [Charge](https://developer.squareup.com/reference/square_2021-08-18/transactions-api/charge) endpoint with a &#x60;delay_capture&#x60; value of &#x60;true&#x60;.   See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture) for more information.

    :param location_id: 
    :type location_id: str
    :param transaction_id: 
    :type transaction_id: str

    """
    return web.Response(status=200)
