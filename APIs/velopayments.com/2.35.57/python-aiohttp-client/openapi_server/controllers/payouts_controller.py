from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_payout_request_v3 import CreatePayoutRequestV3
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server.models.instruct_payout_request_v3 import InstructPayoutRequestV3
from openapi_server.models.paged_payments_response_v3 import PagedPaymentsResponseV3
from openapi_server.models.payout_summary_response_v3 import PayoutSummaryResponseV3
from openapi_server.models.quote_response_v3 import QuoteResponseV3
from openapi_server.models.schedule_payout_request_v3 import SchedulePayoutRequestV3
from openapi_server.models.submit_payout_v3_request import SubmitPayoutV3Request
from openapi_server.models.withdraw_payment_request import WithdrawPaymentRequest
from openapi_server import util


async def create_quote_for_payout_v3(request: web.Request, payout_id) -> web.Response:
    """Create a quote for the payout

    Create quote for a payout

    :param payout_id: Id of the payout
    :type payout_id: str
    :type payout_id: str

    """
    return web.Response(status=200)


async def deschedule_payout(request: web.Request, payout_id) -> web.Response:
    """Deschedule a payout

    Remove the schedule for a scheduled payout

    :param payout_id: Id of the payout
    :type payout_id: str
    :type payout_id: str

    """
    return web.Response(status=200)


async def get_payments_for_payout_v3(request: web.Request, payout_id, status=None, remote_id=None, payor_payment_id=None, source_account_name=None, transmission_type=None, payment_memo=None, page_size=None, page=None) -> web.Response:
    """Retrieve payments for a payout

    Retrieve payments for a payout

    :param payout_id: Id of the payout
    :type payout_id: str
    :type payout_id: str
    :param status: Payment Status * ACCEPTED: any payment which was accepted at submission time (status may have changed since) * REJECTED: any payment rejected by initial submission processing * WITHDRAWN: any payment which has been withdrawn * WITHDRAWABLE: any payment eligible for withdrawal 
    :type status: str
    :param remote_id: The remote id of the payees.
    :type remote_id: str
    :param payor_payment_id: Payor&#39;s Id of the Payment
    :type payor_payment_id: str
    :param source_account_name: Physical Account Name
    :type source_account_name: str
    :param transmission_type: Transmission Type * ACH * SAME_DAY_ACH * WIRE 
    :type transmission_type: str
    :param payment_memo: Payment Memo of the Payment
    :type payment_memo: str
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param page: Page number. Default is 1.
    :type page: int

    """
    return web.Response(status=200)


async def get_payout_summary_v3(request: web.Request, payout_id) -> web.Response:
    """Get Payout Summary

    Get payout summary - returns the current state of the payout.

    :param payout_id: Id of the payout
    :type payout_id: str
    :type payout_id: str

    """
    return web.Response(status=200)


async def instruct_payout_v3(request: web.Request, payout_id, body=None) -> web.Response:
    """Instruct Payout

    Instruct a payout to be made for the specified payoutId.

    :param payout_id: Id of the payout
    :type payout_id: str
    :type payout_id: str
    :param body: Additional instruct payout parameters
    :type body: dict | bytes

    """
    body = InstructPayoutRequestV3.from_dict(body)
    return web.Response(status=200)


async def schedule_for_payout(request: web.Request, payout_id, body=None) -> web.Response:
    """Schedule a payout

    &lt;p&gt;Schedule a payout for auto-instruction in the future or update existing payout schedule if the payout has been scheduled before.&lt;/p&gt; 

    :param payout_id: Id of the payout
    :type payout_id: str
    :type payout_id: str
    :param body: schedule payout parameters
    :type body: dict | bytes

    """
    body = SchedulePayoutRequestV3.from_dict(body)
    return web.Response(status=200)


async def submit_payout_v3(request: web.Request, body) -> web.Response:
    """Submit Payout

    &lt;p&gt;Create a new payout and return a location header with a link to the payout&lt;/p&gt; &lt;p&gt;Basic validation of the payout is performed before returning but more comprehensive validation is done asynchronously&lt;/p&gt; &lt;p&gt;The results can be obtained by issuing a HTTP GET to the URL returned in the location header&lt;/p&gt; &lt;p&gt;**NOTE:** amount values in payments must be in &#39;minor units&#39; format. E.g. cents for USD, pence for GBP etc with no decimal places&lt;/p&gt; 

    :param body: Post amount to transfer using stored funding account details.
    :type body: dict | bytes

    """
    body = CreatePayoutRequestV3.from_dict(body)
    return web.Response(status=200)


async def withdraw_payment(request: web.Request, payment_id, body) -> web.Response:
    """Withdraw a Payment

    &lt;p&gt;withdraw a payment &lt;/p&gt; &lt;p&gt;There are a variety of reasons why this can fail&lt;/p&gt; &lt;ul&gt;     &lt;li&gt;the payment must be in a state of &#39;accepted&#39; or &#39;unfunded&#39;&lt;/li&gt;     &lt;li&gt;the payout must not be in a state of &#39;instructed&#39;&lt;/li&gt; &lt;/ul&gt; 

    :param payment_id: Id of the Payment
    :type payment_id: str
    :type payment_id: str
    :param body: details for withdrawal
    :type body: dict | bytes

    """
    body = WithdrawPaymentRequest.from_dict(body)
    return web.Response(status=200)


async def withdraw_payout_v3(request: web.Request, payout_id) -> web.Response:
    """Withdraw Payout

    Withdraw Payout will remove the payout details from the rails but the payout will still be accessible in payout service in WITHDRAWN status.

    :param payout_id: Id of the payout
    :type payout_id: str
    :type payout_id: str

    """
    return web.Response(status=200)
