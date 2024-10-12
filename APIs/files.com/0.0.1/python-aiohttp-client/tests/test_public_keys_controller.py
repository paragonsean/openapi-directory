# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.public_key_entity import PublicKeyEntity


pytestmark = pytest.mark.asyncio

async def test_delete_public_keys_id(client):
    """Test case for delete_public_keys_id

    Delete Public Key
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/public_keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_keys(client):
    """Test case for get_public_keys

    List Public Keys
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/public_keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_keys_id(client):
    """Test case for get_public_keys_id

    Show Public Key
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/public_keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_public_keys_id(client):
    """Test case for patch_public_keys_id

    Update Public Key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('title', 'title_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/public_keys/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_public_keys(client):
    """Test case for post_public_keys

    Create Public Key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('public_key', 'public_key_example')
    data.add_field('title', 'title_example')
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/public_keys',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

