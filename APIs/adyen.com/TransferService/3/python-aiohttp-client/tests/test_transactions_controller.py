# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_search_response import TransactionSearchResponse


pytestmark = pytest.mark.asyncio

async def test_get_transactions(client):
    """Test case for get_transactions

    Get all transactions
    """
    params = [('balancePlatform', 'balance_platform_example'),
                    ('paymentInstrumentId', 'payment_instrument_id_example'),
                    ('accountHolderId', 'account_holder_id_example'),
                    ('balanceAccountId', 'balance_account_id_example'),
                    ('cursor', 'cursor_example'),
                    ('createdSince', '2013-10-20T19:20:30+01:00'),
                    ('createdUntil', '2013-10-20T19:20:30+01:00'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'clientKey': 'special-key',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/btl/v3/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions_id(client):
    """Test case for get_transactions_id

    Get a transaction
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'clientKey': 'special-key',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/btl/v3/transactions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

