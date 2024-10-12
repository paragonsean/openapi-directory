# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.list_and_search_media_items200_response import ListAndSearchMediaItems200Response
from openapi_server.models.media import Media


pytestmark = pytest.mark.asyncio

async def test_delete_a_media_item(client):
    """Test case for delete_a_media_item

    Delete a media item
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v3/media/:id',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_and_search_media_items(client):
    """Test case for list_and_search_media_items

    List and search media items
    """
    params = [('order', descending),
                    ('page_index', 0),
                    ('page_size', 20),
                    ('start_time', '1 week ago'),
                    ('end_time', '2020-01-01T14:00:00.000Z')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/media/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_a_media_item(client):
    """Test case for retrieve_a_media_item

    Retrieve a media item
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/media/:id/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_update_a_media_item(client):
    """Test case for update_a_media_item

    Update a media item
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('max_downloads_allowed', 56)
    data.add_field('metadata_primary', 'metadata_primary_example')
    data.add_field('metadata_secondary', 'metadata_secondary_example')
    data.add_field('mime_type', 'mime_type_example')
    data.add_field('public', True)
    data.add_field('title', 'title_example')
    response = await client.request(
        method='PUT',
        path='/v3/media/:id/info',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

