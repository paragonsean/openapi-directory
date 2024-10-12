# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.media import Media
from openapi_server.models.media_page import MediaPage
from openapi_server.models.resource_id import ResourceId


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_media(client):
    """Test case for create_media

    Create media
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('name', 'name_example')
    response = await client.request(
        method='POST',
        path='/v2/media',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_media(client):
    """Test case for find_media

    Find media
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', 'filter_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/media',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media(client):
    """Test case for get_media

    Get a specific media
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/media/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_data(client):
    """Test case for get_media_data

    Download media by extension
    """
    headers = { 
        'Accept': 'video/mp4',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/media/{id_extension}'.format(id=56, extension='extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_data_binary(client):
    """Test case for get_media_data_binary

    Download a MP3 media
    """
    headers = { 
        'Accept': 'application/binary',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/media/{id}/file'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_data_by_key(client):
    """Test case for get_media_data_by_key

    Download media by extension
    """
    headers = { 
        'Accept': 'video/mp4',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/media/public/{key_extension}'.format(key='key_example', extension='extension_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

