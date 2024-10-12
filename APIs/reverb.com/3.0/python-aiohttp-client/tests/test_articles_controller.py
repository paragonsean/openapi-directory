# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_articles_categories_get(client):
    """Test case for articles_categories_get

    List of all article categories
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/articles/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_get(client):
    """Test case for articles_get

    
    """
    params = [('page', 1),
                    ('per_page', 24),
                    ('offset', 56),
                    ('query', 'query_example'),
                    ('exclude_featured', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/articles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

