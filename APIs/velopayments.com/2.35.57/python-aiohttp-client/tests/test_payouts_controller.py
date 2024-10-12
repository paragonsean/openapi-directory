# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_create_quote_for_payout_v3(client):
    """Test case for create_quote_for_payout_v3

    Create a quote for the payout
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/payouts/{payout_id}/quote'.format(payout_id='payout_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deschedule_payout(client):
    """Test case for deschedule_payout

    Deschedule a payout
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/payouts/{payout_id}/schedule'.format(payout_id='payout_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments_for_payout_v3(client):
    """Test case for get_payments_for_payout_v3

    Retrieve payments for a payout
    """
    params = [('status', 'status_example'),
                    ('remoteId', 'remote_id_example'),
                    ('payorPaymentId', 'payor_payment_id_example'),
                    ('sourceAccountName', 'source_account_name_example'),
                    ('transmissionType', 'transmission_type_example'),
                    ('paymentMemo', 'payment_memo_example'),
                    ('pageSize', 25),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/payouts/{payout_id}/payments'.format(payout_id='payout_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payout_summary_v3(client):
    """Test case for get_payout_summary_v3

    Get Payout Summary
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/payouts/{payout_id}'.format(payout_id='payout_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_instruct_payout_v3(client):
    """Test case for instruct_payout_v3

    Instruct Payout
    """
    body = {"fxRateDegredationThresholdPercentage":0.8008282}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/payouts/{payout_id}'.format(payout_id='payout_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedule_for_payout(client):
    """Test case for schedule_for_payout

    Schedule a payout
    """
    body = {"notificationsEnabled":True,"scheduledFor":"2025-01-01T10:00:00Z"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/payouts/{payout_id}/schedule'.format(payout_id='payout_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_submit_payout_v3(client):
    """Test case for submit_payout_v3

    Submit Payout
    """
    body = {"payments":[{"amount":1299,"currency":"USD","paymentMemo":"my memo","paymentMetadata":"invoiceeId_123|abc001:12345|xyz002:4567","payorPaymentId":"123211321ABSD","remoteId":"remoteId1234","remoteSystemId":"remoteSystemId","sourceAccountName":"MyAccountName","transmissionType":"ACH"},{"amount":1299,"currency":"USD","paymentMemo":"my memo","paymentMetadata":"invoiceeId_123|abc001:12345|xyz002:4567","payorPaymentId":"123211321ABSD","remoteId":"remoteId1234","remoteSystemId":"remoteSystemId","sourceAccountName":"MyAccountName","transmissionType":"ACH"},{"amount":1299,"currency":"USD","paymentMemo":"my memo","paymentMetadata":"invoiceeId_123|abc001:12345|xyz002:4567","payorPaymentId":"123211321ABSD","remoteId":"remoteId1234","remoteSystemId":"remoteSystemId","sourceAccountName":"MyAccountName","transmissionType":"ACH"},{"amount":1299,"currency":"USD","paymentMemo":"my memo","paymentMetadata":"invoiceeId_123|abc001:12345|xyz002:4567","payorPaymentId":"123211321ABSD","remoteId":"remoteId1234","remoteSystemId":"remoteSystemId","sourceAccountName":"MyAccountName","transmissionType":"ACH"},{"amount":1299,"currency":"USD","paymentMemo":"my memo","paymentMetadata":"invoiceeId_123|abc001:12345|xyz002:4567","payorPaymentId":"123211321ABSD","remoteId":"remoteId1234","remoteSystemId":"remoteSystemId","sourceAccountName":"MyAccountName","transmissionType":"ACH"}],"payoutFromPayorId":"c4261044-13df-4a6c-b1d4-fa8be2b46f5a","payoutMemo":"Monthly Payment","payoutToPayorId":"9afc6b39-de12-466a-a9ca-07c7a23b312d"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/payouts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_withdraw_payment(client):
    """Test case for withdraw_payment

    Withdraw a Payment
    """
    body = {"reason":"Payment submitted in error"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/payments/{payment_id}/withdraw'.format(payment_id='payment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_withdraw_payout_v3(client):
    """Test case for withdraw_payout_v3

    Withdraw Payout
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/payouts/{payout_id}'.format(payout_id='payout_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

