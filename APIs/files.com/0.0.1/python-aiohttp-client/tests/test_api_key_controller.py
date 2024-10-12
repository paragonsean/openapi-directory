# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.api_key_entity import ApiKeyEntity


pytestmark = pytest.mark.asyncio

async def test_api_key_delete_current(client):
    """Test case for api_key_delete_current

    Delete current API key.  (Requires current API connection to be using an API key.)
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/api_key',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_key_find_current(client):
    """Test case for api_key_find_current

    Show information about current API key.  (Requires current API connection to be using an API key.)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/api_key',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_key_update_current(client):
    """Test case for api_key_update_current

    Update current API key.  (Requires current API connection to be using an API key.)
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('expires_at', '2013-10-20T19:20:30+01:00')
    data.add_field('name', 'name_example')
    data.add_field('permission_set', 'permission_set_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/api_key',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

