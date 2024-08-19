# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_pages import TransactionPages


pytestmark = pytest.mark.asyncio

async def test_transactions_get(client):
    """Test case for transactions_get

    Returns a paginated list of transactions
    """
    params = [('query', 'query_example'),
                    ('sort', 'sort_example'),
                    ('pageNumber', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_transaction_id_delete(client):
    """Test case for transactions_transaction_id_delete

    Deleted a transaction
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/transactions/{transaction_id}'.format(transaction_id='transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_transaction_id_get(client):
    """Test case for transactions_transaction_id_get

    Returns a transaction
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/transactions/{transaction_id}'.format(transaction_id='transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transactions_transaction_id_post(client):
    """Test case for transactions_transaction_id_post

    Updates a transaction
    """
    params = [('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/transactions/{transaction_id}'.format(transaction_id='transaction_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

