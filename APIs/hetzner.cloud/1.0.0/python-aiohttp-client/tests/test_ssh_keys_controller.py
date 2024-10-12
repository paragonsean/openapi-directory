# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ssh_keys_get200_response import SshKeysGet200Response
from openapi_server.models.ssh_keys_id_put_request import SshKeysIdPutRequest
from openapi_server.models.ssh_keys_post201_response import SshKeysPost201Response
from openapi_server.models.ssh_keys_post_request import SshKeysPostRequest


pytestmark = pytest.mark.asyncio

async def test_ssh_keys_get(client):
    """Test case for ssh_keys_get

    Get all SSH keys
    """
    params = [('sort', 'sort_example'),
                    ('name', 'name_example'),
                    ('fingerprint', 'fingerprint_example'),
                    ('label_selector', 'label_selector_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/ssh_keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ssh_keys_id_delete(client):
    """Test case for ssh_keys_id_delete

    Delete an SSH key
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v1/ssh_keys/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ssh_keys_id_get(client):
    """Test case for ssh_keys_id_get

    Get a SSH key
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/ssh_keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ssh_keys_id_put(client):
    """Test case for ssh_keys_id_put

    Update an SSH key
    """
    body = openapi_server.SshKeysIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/ssh_keys/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ssh_keys_post(client):
    """Test case for ssh_keys_post

    Create an SSH key
    """
    body = openapi_server.SshKeysPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/ssh_keys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

