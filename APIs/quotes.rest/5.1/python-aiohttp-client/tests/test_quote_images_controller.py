# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

async def test_quote_image_background_delete(client):
    """Test case for quote_image_background_delete

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/quote/image/background',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_background_list_get(client):
    """Test case for quote_image_background_list_get

    
    """
    params = [('start', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/image/background/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_quote_image_background_post(client):
    """Test case for quote_image_background_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('image', '/path/to/file')
    data.add_field('tags', 'tags_example')
    response = await client.request(
        method='POST',
        path='/quote/image/background',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_background_search_get(client):
    """Test case for quote_image_background_search_get

    
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/image/background/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_background_tags_add_post(client):
    """Test case for quote_image_background_tags_add_post

    
    """
    params = [('id', 'id_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/quote/image/background/tags/add',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_background_tags_remove_post(client):
    """Test case for quote_image_background_tags_remove_post

    
    """
    params = [('id', 'id_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/quote/image/background/tags/remove',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_delete(client):
    """Test case for quote_image_delete

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/quote/image',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_font_delete(client):
    """Test case for quote_image_font_delete

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/quote/image/font',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_font_list_get(client):
    """Test case for quote_image_font_list_get

    
    """
    params = [('start', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/image/font/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_quote_image_font_post(client):
    """Test case for quote_image_font_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('font', '/path/to/file')
    data.add_field('tags', 'tags_example')
    response = await client.request(
        method='POST',
        path='/quote/image/font',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_font_search_get(client):
    """Test case for quote_image_font_search_get

    
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/image/font/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_font_tags_add_post(client):
    """Test case for quote_image_font_tags_add_post

    
    """
    params = [('id', 'id_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/quote/image/font/tags/add',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_font_tags_remove_post(client):
    """Test case for quote_image_font_tags_remove_post

    
    """
    params = [('id', 'id_example'),
                    ('tags', 'tags_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/quote/image/font/tags/remove',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_get(client):
    """Test case for quote_image_get

    
    """
    params = [('id', 'id_example'),
                    ('binary', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/image',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_put(client):
    """Test case for quote_image_put

    
    """
    params = [('quote_id', 'quote_id_example'),
                    ('bgimage_id', 'theysaidso_default_background_image'),
                    ('bg_color', 'bg_color_example'),
                    ('font_id', 'theysaidso_default_font'),
                    ('text_color', 'text_color_example'),
                    ('text_size', 'text_size_example'),
                    ('halign', 'center'),
                    ('valign', 'center'),
                    ('width', 56),
                    ('height', 56),
                    ('branding', False),
                    ('include_transparent_layer', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/quote/image',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_image_search_get(client):
    """Test case for quote_image_search_get

    
    """
    params = [('category', 'category_example'),
                    ('author', 'author_example'),
                    ('private', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/quote/image/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

