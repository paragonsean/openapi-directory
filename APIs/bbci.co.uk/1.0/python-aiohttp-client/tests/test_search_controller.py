# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Search
    """
    params = [('q', 'q_example'),
                    ('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_suggest(client):
    """Test case for search_suggest

    Search-suggest
    """
    params = [('q', 'q_example'),
                    ('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/search-suggest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

