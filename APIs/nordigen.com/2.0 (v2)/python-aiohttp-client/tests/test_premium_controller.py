# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_retrieve_account_transactions_v2(client):
    """Test case for retrieve_account_transactions_v2

    
    """
    params = [('country', 'AT'),
                    ('date_from', '2023-01-21'),
                    ('date_to', '2023-04-21')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/accounts/premium/{id}/transactions'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

