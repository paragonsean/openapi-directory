# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_timestags_get(client):
    """Test case for timestags_get

    
    """
    params = [('query', 'query_example'),
                    ('filter', 'filter_example'),
                    ('max', 10)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/suggest/v1/timestags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

