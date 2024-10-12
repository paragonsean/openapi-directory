# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_news(client):
    """Test case for get_news

    Retrieves the latest news whose content contains the query string.
    """
    params = [('query', 'query_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/ai/news',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

