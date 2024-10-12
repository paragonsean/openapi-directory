# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Get a search results
    """
    params = [('q', 'q_example'),
                    ('type', 'type_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/search'.format(namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

