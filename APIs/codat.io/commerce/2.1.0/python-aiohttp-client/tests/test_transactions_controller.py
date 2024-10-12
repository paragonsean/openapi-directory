# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transactions import Transactions


pytestmark = pytest.mark.asyncio

async def test_list_transactions(client):
    """Test case for list_transactions

    List transactions
    """
    params = [('page', 1),
                    ('pageSize', 100),
                    ('query', 'query_example'),
                    ('orderBy', '-modifiedDate')]
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/connections/{connection_id}/data/commerce-transactions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

