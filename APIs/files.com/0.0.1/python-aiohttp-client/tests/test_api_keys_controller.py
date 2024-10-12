# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.api_key_entity import ApiKeyEntity


pytestmark = pytest.mark.asyncio

async def test_delete_api_keys_id(client):
    """Test case for delete_api_keys_id

    Delete Api Key
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/api_keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_keys(client):
    """Test case for get_api_keys

    List Api Keys
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_lt', None),
                    ('filter_lteq', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/api_keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_keys_id(client):
    """Test case for get_api_keys_id

    Show Api Key
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/api_keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_api_keys_id(client):
    """Test case for patch_api_keys_id

    Update Api Key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('expires_at', '2013-10-20T19:20:30+01:00')
    data.add_field('name', 'name_example')
    data.add_field('permission_set', 'permission_set_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/api_keys/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_api_keys(client):
    """Test case for post_api_keys

    Create Api Key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('expires_at', '2013-10-20T19:20:30+01:00')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    data.add_field('permission_set', full)
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/api_keys',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

