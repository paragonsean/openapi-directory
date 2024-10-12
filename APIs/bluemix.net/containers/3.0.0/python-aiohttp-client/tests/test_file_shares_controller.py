# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fileshare import Fileshare
from openapi_server.models.fileshare_param import FileshareParam
from openapi_server.models.get_fileshare_details import GetFileshareDetails


pytestmark = pytest.mark.asyncio

async def test_volumes_fs_create_post(client):
    """Test case for volumes_fs_create_post

    Create a file share in a space
    """
    body = {"fsIOPS":0.8008281904610115,"fsSize":6,"fsName":"fsName"}
    headers = { 
        'Content-Type': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='POST',
        path='/v3/volumes/fs/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_fs_flavors_json_get(client):
    """Test case for volumes_fs_flavors_json_get

    List available file share sizes
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/volumes/fs/flavors/json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_fs_json_get(client):
    """Test case for volumes_fs_json_get

    List available file shares in a space
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/volumes/fs/json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_fs_name_delete(client):
    """Test case for volumes_fs_name_delete

    Delete a file share
    """
    headers = { 
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/volumes/fs/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volumes_fs_name_json_get(client):
    """Test case for volumes_fs_name_json_get

    Inspect a file share
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/volumes/fs/{name}/json'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

