from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_fundings_response import GetFundingsResponse
from openapi_server.models.get_payments_for_payout_response_v3 import GetPaymentsForPayoutResponseV3
from openapi_server.models.get_payout_statistics import GetPayoutStatistics
from openapi_server.models.get_payouts_response_v3 import GetPayoutsResponseV3
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.list_payments_response_v3 import ListPaymentsResponseV3
from openapi_server.models.payment_delta_response_v1 import PaymentDeltaResponseV1
from openapi_server.models.payment_response_v3 import PaymentResponseV3
from openapi_server.models.payor_aml_transaction_v3 import PayorAmlTransactionV3
from openapi_server import util


async def export_transactions_csvv3(request: web.Request, payor_id=None, start_date=None, end_date=None) -> web.Response:
    """V3 Export Transactions

    Deprecated (use /v4/paymentaudit/transactions instead)

    :param payor_id: The Payor ID for whom you wish to run the report. For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor. 
    :type payor_id: str
    :type payor_id: str
    :param start_date: Start date, inclusive. Format is YYYY-MM-DD
    :type start_date: str
    :param end_date: End date, inclusive. Format is YYYY-MM-DD
    :type end_date: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def get_fundings_v1(request: web.Request, payor_id, page=None, page_size=None, sort=None) -> web.Response:
    """V1 Get Fundings for Payor

    Deprecated (use /v4/paymentaudit/fundings)

    :param payor_id: The account owner Payor ID
    :type payor_id: str
    :type payor_id: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields. Example: &#x60;&#x60;&#x60;?sort&#x3D;destinationCurrency:asc,destinationAmount:asc&#x60;&#x60;&#x60; Default is no sort. The supported sort fields are: dateTime and amount. 
    :type sort: str

    """
    return web.Response(status=200)


async def get_payment_details_v3(request: web.Request, payment_id, sensitive=None) -> web.Response:
    """V3 Get Payment

    Deprecated (use /v4/paymentaudit/payments/&lt;paymentId&gt; instead)

    :param payment_id: Payment Id
    :type payment_id: str
    :type payment_id: str
    :param sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    :type sensitive: bool

    """
    return web.Response(status=200)


async def get_payments_for_payout_pav3(request: web.Request, payout_id, remote_id=None, status=None, source_amount_from=None, source_amount_to=None, payment_amount_from=None, payment_amount_to=None, submitted_date_from=None, submitted_date_to=None, page=None, page_size=None, sort=None, sensitive=None) -> web.Response:
    """V3 Get Payments for Payout

    Deprecated (use /v4/paymentaudit/payouts/&lt;payoutId&gt; instead)

    :param payout_id: The id (UUID) of the payout.
    :type payout_id: str
    :type payout_id: str
    :param remote_id: The remote id of the payees.
    :type remote_id: str
    :param status: Payment Status
    :type status: str
    :param source_amount_from: The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom
    :type source_amount_from: int
    :param source_amount_to: The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo
    :type source_amount_to: int
    :param payment_amount_from: The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom
    :type payment_amount_from: int
    :param payment_amount_to: The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo
    :type payment_amount_to: int
    :param submitted_date_from: The submitted date from range filter. Format is yyyy-MM-dd.
    :type submitted_date_from: str
    :param submitted_date_to: The submitted date to range filter. Format is yyyy-MM-dd.
    :type submitted_date_to: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: &lt;p&gt;List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId&lt;/p&gt; &lt;p&gt;The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status&lt;/p&gt; 
    :type sort: str
    :param sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    :type sensitive: bool

    """
    submitted_date_from = util.deserialize_date(submitted_date_from)
    submitted_date_to = util.deserialize_date(submitted_date_to)
    return web.Response(status=200)


async def get_payout_stats_v1(request: web.Request, payor_id=None) -> web.Response:
    """V1 Get Payout Statistics

    Deprecated (Use /v4/paymentaudit/payoutStatistics)

    :param payor_id: The account owner Payor ID. Required for external users.
    :type payor_id: str
    :type payor_id: str

    """
    return web.Response(status=200)


async def get_payouts_for_payor_v3(request: web.Request, payor_id, payout_memo=None, status=None, submitted_date_from=None, submitted_date_to=None, page=None, page_size=None, sort=None) -> web.Response:
    """V3 Get Payouts for Payor

    Deprecated (use /v4/paymentaudit/payouts instead)

    :param payor_id: The account owner Payor ID
    :type payor_id: str
    :type payor_id: str
    :param payout_memo: Payout Memo filter - case insensitive sub-string match
    :type payout_memo: str
    :param status: Payout Status
    :type status: str
    :param submitted_date_from: The submitted date from range filter. Format is yyyy-MM-dd.
    :type submitted_date_from: str
    :param submitted_date_to: The submitted date to range filter. Format is yyyy-MM-dd.
    :type submitted_date_to: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status. 
    :type sort: str

    """
    submitted_date_from = util.deserialize_date(submitted_date_from)
    submitted_date_to = util.deserialize_date(submitted_date_to)
    return web.Response(status=200)


async def list_payment_changes(request: web.Request, payor_id, updated_since, page=None, page_size=None) -> web.Response:
    """V1 List Payment Changes

    Deprecated (use /v4/payments/deltas instead)

    :param payor_id: The Payor ID to find associated Payments
    :type payor_id: str
    :type payor_id: str
    :param updated_since: The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    :type updated_since: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int

    """
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def list_payments_audit_v3(request: web.Request, payee_id=None, payor_id=None, payor_name=None, remote_id=None, status=None, source_account_name=None, source_amount_from=None, source_amount_to=None, source_currency=None, payment_amount_from=None, payment_amount_to=None, payment_currency=None, submitted_date_from=None, submitted_date_to=None, payment_memo=None, page=None, page_size=None, sort=None, sensitive=None) -> web.Response:
    """V3 Get List of Payments

    Deprecated (use /v4/paymentaudit/payments instead)

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param payor_id: The account owner Payor Id. Required for external users.
    :type payor_id: str
    :type payor_id: str
    :param payor_name: The payor’s name. This filters via a case insensitive substring match.
    :type payor_name: str
    :param remote_id: The remote id of the payees.
    :type remote_id: str
    :param status: Payment Status
    :type status: str
    :param source_account_name: The source account name filter. This filters via a case insensitive substring match.
    :type source_account_name: str
    :param source_amount_from: The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom
    :type source_amount_from: int
    :param source_amount_to: The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo
    :type source_amount_to: int
    :param source_currency: The source currency filter. Filters based on an exact match on the currency.
    :type source_currency: str
    :param payment_amount_from: The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom
    :type payment_amount_from: int
    :param payment_amount_to: The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo
    :type payment_amount_to: int
    :param payment_currency: The payment currency filter. Filters based on an exact match on the currency.
    :type payment_currency: str
    :param submitted_date_from: The submitted date from range filter. Format is yyyy-MM-dd.
    :type submitted_date_from: str
    :param submitted_date_to: The submitted date to range filter. Format is yyyy-MM-dd.
    :type submitted_date_to: str
    :param payment_memo: The payment memo filter. This filters via a case insensitive substring match.
    :type payment_memo: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status 
    :type sort: str
    :param sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    :type sensitive: bool

    """
    submitted_date_from = util.deserialize_date(submitted_date_from)
    submitted_date_to = util.deserialize_date(submitted_date_to)
    return web.Response(status=200)
