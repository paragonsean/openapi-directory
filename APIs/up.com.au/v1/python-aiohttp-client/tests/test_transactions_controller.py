# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_transaction_response import GetTransactionResponse
from openapi_server.models.list_transactions_response import ListTransactionsResponse
from openapi_server.models.transaction_status_enum import TransactionStatusEnum


pytestmark = pytest.mark.asyncio

async def test_accounts_account_id_transactions_get(client):
    """Test case for accounts_account_id_transactions_get

    List transactions by account
    """
    params = [('page[size]', 30),
                    ('filter[status]', openapi_server.TransactionStatusEnum()),
                    ('filter[since]', '2020-01-01T01:02:03+10:00'),
                    ('filter[until]', '2020-02-01T01:02:03+10:00'),
                    ('filter[category]', 'good-life'),
                    ('filter[tag]', 'Holiday')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{account_id}/transactions'.format(account_id='b5544658-4bbd-4eb1-8f63-a9909e0f564b'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_get(client):
    """Test case for transactions_get

    List transactions
    """
    params = [('page[size]', 30),
                    ('filter[status]', openapi_server.TransactionStatusEnum()),
                    ('filter[since]', '2020-01-01T01:02:03+10:00'),
                    ('filter[until]', '2020-02-01T01:02:03+10:00'),
                    ('filter[category]', 'good-life'),
                    ('filter[tag]', 'Holiday')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_id_get(client):
    """Test case for transactions_id_get

    Retrieve transaction
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transactions/{id}'.format(id='7a9d19f9-106c-4e29-8591-52fc5d8f09c5'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

