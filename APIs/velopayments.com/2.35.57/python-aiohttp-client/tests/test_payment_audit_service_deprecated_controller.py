# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_export_transactions_csvv3(client):
    """Test case for export_transactions_csvv3

    V3 Export Transactions
    """
    params = [('payorId', 'payor_id_example'),
                    ('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/paymentaudit/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fundings_v1(client):
    """Test case for get_fundings_v1

    V1 Get Fundings for Payor
    """
    params = [('payorId', 'payor_id_example'),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/paymentaudit/fundings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_details_v3(client):
    """Test case for get_payment_details_v3

    V3 Get Payment
    """
    params = [('sensitive', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/paymentaudit/payments/{payment_id}'.format(payment_id='payment_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments_for_payout_pav3(client):
    """Test case for get_payments_for_payout_pav3

    V3 Get Payments for Payout
    """
    params = [('remoteId', 'remote_id_example'),
                    ('status', 'status_example'),
                    ('sourceAmountFrom', 56),
                    ('sourceAmountTo', 56),
                    ('paymentAmountFrom', 56),
                    ('paymentAmountTo', 56),
                    ('submittedDateFrom', '2013-10-20'),
                    ('submittedDateTo', '2013-10-20'),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'sort_example'),
                    ('sensitive', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/paymentaudit/payouts/{payout_id}'.format(payout_id='payout_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payout_stats_v1(client):
    """Test case for get_payout_stats_v1

    V1 Get Payout Statistics
    """
    params = [('payorId', 'payor_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/paymentaudit/payoutStatistics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payouts_for_payor_v3(client):
    """Test case for get_payouts_for_payor_v3

    V3 Get Payouts for Payor
    """
    params = [('payorId', 'payor_id_example'),
                    ('payoutMemo', 'payout_memo_example'),
                    ('status', 'status_example'),
                    ('submittedDateFrom', '2013-10-20'),
                    ('submittedDateTo', '2013-10-20'),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/paymentaudit/payouts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payment_changes(client):
    """Test case for list_payment_changes

    V1 List Payment Changes
    """
    params = [('payorId', 'payor_id_example'),
                    ('updatedSince', '2013-10-20T19:20:30+01:00'),
                    ('page', 1),
                    ('pageSize', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/deltas/payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payments_audit_v3(client):
    """Test case for list_payments_audit_v3

    V3 Get List of Payments
    """
    params = [('payeeId', 'payee_id_example'),
                    ('payorId', 'payor_id_example'),
                    ('payorName', 'payor_name_example'),
                    ('remoteId', 'remote_id_example'),
                    ('status', 'status_example'),
                    ('sourceAccountName', 'source_account_name_example'),
                    ('sourceAmountFrom', 56),
                    ('sourceAmountTo', 56),
                    ('sourceCurrency', 'source_currency_example'),
                    ('paymentAmountFrom', 56),
                    ('paymentAmountTo', 56),
                    ('paymentCurrency', 'payment_currency_example'),
                    ('submittedDateFrom', '2013-10-20'),
                    ('submittedDateTo', '2013-10-20'),
                    ('paymentMemo', 'payment_memo_example'),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'sort_example'),
                    ('sensitive', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/paymentaudit/payments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

