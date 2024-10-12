from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_fundings_response import GetFundingsResponse
from openapi_server.models.get_payments_for_payout_response_v4 import GetPaymentsForPayoutResponseV4
from openapi_server.models.get_payout_statistics import GetPayoutStatistics
from openapi_server.models.get_payouts_response import GetPayoutsResponse
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.list_payments_response_v4 import ListPaymentsResponseV4
from openapi_server.models.payment_delta_response import PaymentDeltaResponse
from openapi_server.models.payment_response_v4 import PaymentResponseV4
from openapi_server.models.payor_aml_transaction import PayorAmlTransaction
from openapi_server import util


async def export_transactions_csvv4(request: web.Request, payor_id=None, start_date=None, end_date=None, include=None) -> web.Response:
    """Export Transactions

    Download a CSV file containing payments in a date range. Uses Transfer-Encoding - chunked to stream to the client. Date range is inclusive of both the start and end dates.

    :param payor_id: &lt;p&gt;The Payor ID for whom you wish to run the report.&lt;/p&gt; &lt;p&gt;For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.&lt;/p&gt; 
    :type payor_id: str
    :type payor_id: str
    :param start_date: Start date, inclusive. Format is YYYY-MM-DD
    :type start_date: str
    :param end_date: End date, inclusive. Format is YYYY-MM-DD
    :type end_date: str
    :param include: &lt;p&gt;Mode to determine whether to include other Payor&#39;s data in the results.&lt;/p&gt; &lt;p&gt;May only be used if payorId is specified.&lt;/p&gt; &lt;p&gt;Can be omitted or set to &#39;payorOnly&#39; or &#39;payorAndDescendants&#39;.&lt;/p&gt; &lt;p&gt;payorOnly: Only include results for the specified Payor. This is the default if &#39;include&#39; is omitted.&lt;/p&gt; &lt;p&gt;payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.&lt;/p&gt; &lt;p&gt;Note when a Payor requests the report and include&#x3D;payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id&lt;/p&gt; 
    :type include: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def get_fundings_v4(request: web.Request, payor_id, source_account_name=None, page=None, page_size=None, sort=None) -> web.Response:
    """Get Fundings for Payor

    &lt;p&gt;Get a list of Fundings for a payor.&lt;/p&gt; 

    :param payor_id: The account owner Payor ID
    :type payor_id: str
    :type payor_id: str
    :param source_account_name: The source account name
    :type source_account_name: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields. Example: &#x60;&#x60;&#x60;?sort&#x3D;destinationCurrency:asc,destinationAmount:asc&#x60;&#x60;&#x60; Default is no sort. The supported sort fields are: dateTime and amount. 
    :type sort: str

    """
    return web.Response(status=200)


async def get_payment_details_v4(request: web.Request, payment_id, sensitive=None) -> web.Response:
    """Get Payment

    Get the payment with the given id. This contains the payment history. 

    :param payment_id: Payment Id
    :type payment_id: str
    :type payment_id: str
    :param sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    :type sensitive: bool

    """
    return web.Response(status=200)


async def get_payments_for_payout_v4(request: web.Request, payout_id, rails_id=None, remote_id=None, remote_system_id=None, status=None, source_amount_from=None, source_amount_to=None, payment_amount_from=None, payment_amount_to=None, submitted_date_from=None, submitted_date_to=None, transmission_type=None, page=None, page_size=None, sort=None, sensitive=None) -> web.Response:
    """Get Payments for Payout

    Get List of payments for Payout, allowing for RETURNED status 

    :param payout_id: The id (UUID) of the payout.
    :type payout_id: str
    :type payout_id: str
    :param rails_id: Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the &#39;Get Supported Rails&#39; endpoint. 
    :type rails_id: str
    :param remote_id: The remote id of the payees.
    :type remote_id: str
    :param remote_system_id: The id of the remote system that is orchestrating payments
    :type remote_system_id: str
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
    :param transmission_type: Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO 
    :type transmission_type: str
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


async def get_payout_stats_v4(request: web.Request, payor_id=None) -> web.Response:
    """Get Payout Statistics

    &lt;p&gt;Get payout statistics for a payor.&lt;/p&gt; 

    :param payor_id: The account owner Payor ID. Required for external users.
    :type payor_id: str
    :type payor_id: str

    """
    return web.Response(status=200)


async def get_payouts_for_payor_v4(request: web.Request, payor_id=None, payout_memo=None, status=None, submitted_date_from=None, submitted_date_to=None, from_payor_name=None, scheduled_for_date_from=None, scheduled_for_date_to=None, schedule_status=None, page=None, page_size=None, sort=None) -> web.Response:
    """Get Payouts for Payor

    Get List of payouts for payor 

    :param payor_id: The id (UUID) of the payor funding the payout or the payor whose payees are being paid.
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
    :param from_payor_name: The name of the payor whose payees are being paid. This filters via a case insensitive substring match.
    :type from_payor_name: str
    :param scheduled_for_date_from: Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd.
    :type scheduled_for_date_from: str
    :param scheduled_for_date_to: Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd.
    :type scheduled_for_date_to: str
    :param schedule_status: Payout Schedule Status
    :type schedule_status: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId, scheduledFor 
    :type sort: str

    """
    submitted_date_from = util.deserialize_date(submitted_date_from)
    submitted_date_to = util.deserialize_date(submitted_date_to)
    scheduled_for_date_from = util.deserialize_date(scheduled_for_date_from)
    scheduled_for_date_to = util.deserialize_date(scheduled_for_date_to)
    return web.Response(status=200)


async def list_payment_changes_v4(request: web.Request, payor_id, updated_since, page=None, page_size=None) -> web.Response:
    """List Payment Changes

    Get a paginated response listing payment changes.

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


async def list_payments_audit_v4(request: web.Request, payee_id=None, payor_id=None, payor_name=None, remote_id=None, remote_system_id=None, status=None, transmission_type=None, source_account_name=None, source_amount_from=None, source_amount_to=None, source_currency=None, payment_amount_from=None, payment_amount_to=None, payment_currency=None, submitted_date_from=None, submitted_date_to=None, payment_memo=None, rails_id=None, scheduled_for_date_from=None, scheduled_for_date_to=None, schedule_status=None, post_instruct_fx_status=None, page=None, page_size=None, sort=None, sensitive=None) -> web.Response:
    """Get List of Payments

    Get payments for the given payor Id

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
    :param remote_system_id: The id of the remote system that is orchestrating payments
    :type remote_system_id: str
    :param status: Payment Status
    :type status: str
    :param transmission_type: Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO 
    :type transmission_type: str
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
    :param rails_id: Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the &#39;Get Supported Rails&#39; endpoint. 
    :type rails_id: str
    :param scheduled_for_date_from: Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd.
    :type scheduled_for_date_from: str
    :param scheduled_for_date_to: Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd.
    :type scheduled_for_date_to: str
    :param schedule_status: Payout Schedule Status
    :type schedule_status: str
    :param post_instruct_fx_status: The status of the post instruct FX step if one was required for the payment
    :type post_instruct_fx_status: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by submittedDateTime:desc,paymentId:asc The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime, status and paymentId 
    :type sort: str
    :param sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    :type sensitive: bool

    """
    submitted_date_from = util.deserialize_date(submitted_date_from)
    submitted_date_to = util.deserialize_date(submitted_date_to)
    scheduled_for_date_from = util.deserialize_date(scheduled_for_date_from)
    scheduled_for_date_to = util.deserialize_date(scheduled_for_date_to)
    return web.Response(status=200)
