# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_priceguide_id_transactions_summary_get(client):
    """Test case for priceguide_id_transactions_summary_get

    Get a summary of transactions for a given price guide
    """
    params = [('number_of_months', 3),
                    ('condition', 'used')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/priceguide/{id}/transactions/summary'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

