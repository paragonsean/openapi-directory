# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.quote_response import QuoteResponse


pytestmark = pytest.mark.asyncio

async def test_quote_delete(client):
    """Test case for quote_delete

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/quote',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_get_0(client):
    """Test case for quote_get_0

    
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

async def test_quote_list_get(client):
    """Test case for quote_list_get

    
    """
    params = [('start', 0),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_patch(client):
    """Test case for quote_patch

    
    """
    params = [('id', 'id_example'),
                    ('quote', 'quote_example'),
                    ('author', 'author_example'),
                    ('language', 'en'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/quote',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_post(client):
    """Test case for quote_post

    
    """
    params = [('quote', 'quote_example'),
                    ('author', 'author_example'),
                    ('tags', 'tags_example'),
                    ('language', 'en')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/quote',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_put(client):
    """Test case for quote_put

    
    """
    params = [('quote', 'quote_example'),
                    ('author', 'author_example'),
                    ('tags', 'tags_example'),
                    ('language', 'en')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/quote',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_tags_add_post(client):
    """Test case for quote_tags_add_post

    
    """
    params = [('id', 'id_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/quote/tags/add',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_tags_remove_post(client):
    """Test case for quote_tags_remove_post

    
    """
    params = [('id', 'id_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/quote/tags/remove',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

