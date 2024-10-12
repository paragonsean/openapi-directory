# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.sftp_host_key_entity import SftpHostKeyEntity


pytestmark = pytest.mark.asyncio

async def test_delete_sftp_host_keys_id(client):
    """Test case for delete_sftp_host_keys_id

    Delete Sftp Host Key
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/sftp_host_keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sftp_host_keys(client):
    """Test case for get_sftp_host_keys

    List Sftp Host Keys
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/sftp_host_keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sftp_host_keys_id(client):
    """Test case for get_sftp_host_keys_id

    Show Sftp Host Key
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/sftp_host_keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_sftp_host_keys_id(client):
    """Test case for patch_sftp_host_keys_id

    Update Sftp Host Key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('name', 'name_example')
    data.add_field('private_key', 'private_key_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/sftp_host_keys/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_sftp_host_keys(client):
    """Test case for post_sftp_host_keys

    Create Sftp Host Key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('name', 'name_example')
    data.add_field('private_key', 'private_key_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/sftp_host_keys',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

