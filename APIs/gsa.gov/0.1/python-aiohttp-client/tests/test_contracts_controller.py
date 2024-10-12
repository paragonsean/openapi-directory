# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_list_contracts_get(client):
    """Test case for list_contracts_get

    This endpoint returns contract history from FPDS for a specific vendor
    """
    params = [('duns', 'duns_example'),
                    ('naics', 'naics_example'),
                    ('sort', 'sort_example'),
                    ('direction', 'direction_example'),
                    ('page', 'page_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/api/contracts/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

