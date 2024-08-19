# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_movies_search_search(client):
    """Test case for movies_search_search

    
    """
    params = [('q', 'q_example'),
                    ('page_limit', '10'),
                    ('page', '1')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/movies.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

