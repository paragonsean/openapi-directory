# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.card_transactionsv1 import CardTransactionsv1
from openapi_server.models.card_transactionsv3 import CardTransactionsv3


pytestmark = pytest.mark.asyncio

async def test_get_transactions_by_account_id_filtered(client):
    """Test case for get_transactions_by_account_id_filtered

    Filtered list of transactions for an account (v1)
    """
    params = [('dateRangeFrom', 56),
                    ('dateRangeTo', 56),
                    ('searchKeyword', 'search_keyword_example'),
                    ('transactionTypes', ['transaction_types_example']),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/accounts/{ican}/transactions/filter'.format(ican=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions_by_account_idv1(client):
    """Test case for get_transactions_by_account_idv1

    List transactions for an account (v1)
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/accounts/{ican}/transactions'.format(ican=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transactions_by_account_idv3(client):
    """Test case for get_transactions_by_account_idv3

    List transactions for an account (v3)
    """
    params = [('limit', 56),
                    ('dateRangeFrom', 56),
                    ('dateRangeTo', 56),
                    ('startAfter', 'start_after_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v3/accounts/{ican}/transactions'.format(ican=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

