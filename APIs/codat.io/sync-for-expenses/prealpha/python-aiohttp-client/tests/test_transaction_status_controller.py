# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transaction_metadata import TransactionMetadata
from openapi_server.models.transaction_metadata_list import TransactionMetadataList


pytestmark = pytest.mark.asyncio

async def test_get_sync_transaction(client):
    """Test case for get_sync_transaction

    Get Sync Transaction
    """
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/sync/expenses/syncs/{sync_id}/transactions/{transaction_id}'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002', sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002', transaction_id='336694d8-2dca-4cb5-a28d-3ccb83e55eee'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sync_transactions(client):
    """Test case for list_sync_transactions

    Get Sync transactions
    """
    params = [('page', 1),
                    ('pageSize', 100)]
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/sync/expenses/syncs/{sync_id}/transactions'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002', sync_id='6fb40d5e-b13e-11ed-afa1-0242ac120002'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

