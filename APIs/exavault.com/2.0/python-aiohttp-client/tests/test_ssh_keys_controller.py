# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_ssh_key_request_body import AddSSHKeyRequestBody
from openapi_server.models.ssh_key_collection_response import SSHKeyCollectionResponse
from openapi_server.models.ssh_key_response import SSHKeyResponse


pytestmark = pytest.mark.asyncio

async def test_add_ssh_key(client):
    """Test case for add_ssh_key

    Create a new SSH Key
    """
    body = {"publicKey":"publicKey","userId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ssh-keys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_ssh_key(client):
    """Test case for delete_ssh_key

    Delete an SSH Key
    """
    headers = { 
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/ssh-keys/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ssh_key(client):
    """Test case for get_ssh_key

    Get metadata for an SSH Key
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ssh-keys/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ssh_keys_list(client):
    """Test case for get_ssh_keys_list

    Get metadata for a list of SSH Keys
    """
    params = [('userId', 'user_id_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ssh-keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

