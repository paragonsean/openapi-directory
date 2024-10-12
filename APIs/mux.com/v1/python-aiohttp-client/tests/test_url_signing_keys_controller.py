# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_signing_keys_response import ListSigningKeysResponse
from openapi_server.models.signing_key_response import SigningKeyResponse


pytestmark = pytest.mark.asyncio

async def test_create_url_signing_key(client):
    """Test case for create_url_signing_key

    Create a URL signing key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/signing-keys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_url_signing_key(client):
    """Test case for delete_url_signing_key

    Delete a URL signing key
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/signing-keys/{signing_key_id}'.format(signing_key_id='signing_key_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_url_signing_key(client):
    """Test case for get_url_signing_key

    Retrieve a URL signing key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/signing-keys/{signing_key_id}'.format(signing_key_id='signing_key_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_url_signing_keys(client):
    """Test case for list_url_signing_keys

    List URL signing keys
    """
    params = [('limit', 25),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/signing-keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

