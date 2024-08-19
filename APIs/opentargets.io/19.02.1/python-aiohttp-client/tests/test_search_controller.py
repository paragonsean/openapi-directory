# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_search_0(client):
    """Test case for get_search_0

    Search for a disease or a target
    """
    params = [('q', 'q_example'),
                    ('size', 'size_example'),
                    ('from', '_from_example'),
                    ('filter', 'filter_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

