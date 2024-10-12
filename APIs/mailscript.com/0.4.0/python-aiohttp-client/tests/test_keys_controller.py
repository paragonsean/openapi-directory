# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_key_request import AddKeyRequest
from openapi_server.models.add_key_response import AddKeyResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_keys_response import GetAllKeysResponse
from openapi_server.models.key import Key
from openapi_server.models.update_key_request import UpdateKeyRequest


pytestmark = pytest.mark.asyncio

async def test_add_key(client):
    """Test case for add_key

    Add address key
    """
    body = {"read":True,"name":"name","write":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/addresses/{address}/keys'.format(address='address_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_key(client):
    """Test case for delete_key

    Delete address key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/addresses/{address}/keys/{key}'.format(address='address_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_keys(client):
    """Test case for get_all_keys

    List address keys
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/addresses/{address}/keys'.format(address='address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_key(client):
    """Test case for get_key

    Get address key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/addresses/{address}/keys/{key}'.format(address='address_example', key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_key(client):
    """Test case for update_key

    Update an address key
    """
    body = {"read":True,"name":"name","write":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/addresses/{address}/keys/{key}'.format(address='address_example', key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

