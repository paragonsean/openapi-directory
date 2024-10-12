# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quote_response import QuoteResponse


pytestmark = pytest.mark.asyncio

async def test_quote_authors_popular_get(client):
    """Test case for quote_authors_popular_get

    
    """
    params = [('language', 'en'),
                    ('detailed', False),
                    ('start', 0),
                    ('limit', 5)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/authors/popular',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_authors_search_get(client):
    """Test case for quote_authors_search_get

    
    """
    params = [('query', 'query_example'),
                    ('language', 'en'),
                    ('detailed', False),
                    ('start', 0),
                    ('limit', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/authors/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_bookmark_toggle_get(client):
    """Test case for quote_bookmark_toggle_get

    
    """
    params = [('quote_id', 'quote_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/bookmark/toggle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_categories_popular_get(client):
    """Test case for quote_categories_popular_get

    
    """
    params = [('start', 0),
                    ('limit', 5)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/categories/popular',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_categories_search_get(client):
    """Test case for quote_categories_search_get

    
    """
    params = [('query', '0'),
                    ('start', 0),
                    ('limit', 2)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/categories/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_get(client):
    """Test case for quote_get

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_like_toggle_get(client):
    """Test case for quote_like_toggle_get

    
    """
    params = [('quote_id', 'quote_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/like/toggle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_random_get(client):
    """Test case for quote_random_get

    
    """
    params = [('language', 'en'),
                    ('limit', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/random',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_search_get(client):
    """Test case for quote_search_get

    
    """
    params = [('category', 'category_example'),
                    ('author', 'author_example'),
                    ('minlength', 100),
                    ('maxlength', 300),
                    ('query', 'query_example'),
                    ('private', False),
                    ('language', 'en'),
                    ('limit', 1),
                    ('sfw', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

