# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.feature import Feature


pytestmark = pytest.mark.asyncio

async def test_features_get(client):
    """Test case for features_get

    Query features
    """
    params = [('limit', 3.4),
                    ('start', 3.4),
                    ('order_dir', 'order_dir_example'),
                    ('is_private', True),
                    ('wanted_by', 56),
                    ('order_by', 'order_by_example'),
                    ('tags', 'tags_example'),
                    ('products', 'products_example')]
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/features',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_id_get(client):
    """Test case for features_id_get

    Get a Feature by ID
    """
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/features/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_id_tags_delete(client):
    """Test case for features_id_tags_delete

    Delete custom Feature tags
    """
    headers = { 
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/features/{id}/tags'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_features_id_tags_get(client):
    """Test case for features_id_tags_get

    Get custom Feature tags
    """
    headers = { 
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/features/{id}/tags'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_features_id_tags_post(client):
    """Test case for features_id_tags_post

    Overwrite current custom Feature tags with the given tags
    """
    tags = None
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/features/{id}/tags'.format(id=3.4),
        headers=headers,
        json=tags,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_get(client):
    """Test case for search_get

    Search features
    """
    params = [('scope', 'scope_example'),
                    ('q', 'q_example'),
                    ('status', 'status_example'),
                    ('tags', 'tags_example'),
                    ('products', 'products_example')]
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

