# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.joke_response import JokeResponse


pytestmark = pytest.mark.asyncio

async def test_joke_categories_search_get(client):
    """Test case for joke_categories_search_get

    
    """
    params = [('query', 'query_example'),
                    ('start', 0)]
    headers = { 
        'Accept': 'application/json',
        'X-JokesOne-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/joke/categories/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_joke_delete(client):
    """Test case for joke_delete

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'X-JokesOne-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/joke',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_joke_get(client):
    """Test case for joke_get

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'X-JokesOne-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/joke',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_joke_list_get(client):
    """Test case for joke_list_get

    
    """
    params = [('start', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/joke/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_joke_patch(client):
    """Test case for joke_patch

    
    """
    params = [('id', 'id_example'),
                    ('title', 'title_example'),
                    ('text', 'text_example'),
                    ('author', 'author_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/joke',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_joke_put(client):
    """Test case for joke_put

    
    """
    params = [('title', 'title_example'),
                    ('text', 'text_example'),
                    ('author', 'author_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/joke',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_joke_random_get(client):
    """Test case for joke_random_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/joke/random',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_joke_search_get(client):
    """Test case for joke_search_get

    
    """
    params = [('category', 'category_example'),
                    ('query', 'query_example'),
                    ('minlength', 100),
                    ('maxlength', 300),
                    ('author', 'author_example'),
                    ('private', False)]
    headers = { 
        'Accept': 'application/json',
        'X-JokesOne-Api-Secret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/joke/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_joke_tags_add_post(client):
    """Test case for joke_tags_add_post

    
    """
    params = [('id', 'id_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/joke/tags/add',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_joke_tags_remove_post(client):
    """Test case for joke_tags_remove_post

    
    """
    params = [('id', 'id_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/joke/tags/remove',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

