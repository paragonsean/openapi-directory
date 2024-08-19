# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_volume import UpdateVolume
from openapi_server.models.volume import Volume


pytestmark = pytest.mark.asyncio

async def test_volumes_create_post(client):
    """Test case for volumes_create_post

    Create a volume in a space
    """
    params = [('name', 'name_example'),
                    ('fsName', 'fs_name_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/volumes/create',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_json_get(client):
    """Test case for volumes_json_get

    List all volumes for a space
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/volumes/json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_name_delete(client):
    """Test case for volumes_name_delete

    Delete a volume
    """
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/volumes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_name_json_get(client):
    """Test case for volumes_name_json_get

    Retrieve detailed information about a volume. 
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/volumes/{name}/json'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_name_post(client):
    """Test case for volumes_name_post

    Share a volume with another space
    """
    body = {"removeSpaces":["removeSpaces","removeSpaces"],"addSpaces":["addSpaces","addSpaces"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/volumes/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

