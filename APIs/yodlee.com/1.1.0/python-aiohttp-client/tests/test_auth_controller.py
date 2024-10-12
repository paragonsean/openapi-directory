# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_key_request import ApiKeyRequest
from openapi_server.models.api_key_response import ApiKeyResponse
from openapi_server.models.client_credential_token_response import ClientCredentialTokenResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_delete_api_key(client):
    """Test case for delete_api_key

    Delete API Key
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/auth/apiKey/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_token(client):
    """Test case for delete_token

    Delete Token
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/auth/token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_access_token(client):
    """Test case for generate_access_token

    Generate Access Token
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/auth/token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_api_key(client):
    """Test case for generate_api_key

    Generate API Key
    """
    body = {"publicKey":"publicKey"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/apiKey',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_keys(client):
    """Test case for get_api_keys

    Get API Keys
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/auth/apiKey',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

