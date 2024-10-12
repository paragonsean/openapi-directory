# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_api_secret400_response import CreateAPISecret400Response
from openapi_server.models.create_secret_request import CreateSecretRequest
from openapi_server.models.error_api_key_not_found import ErrorAPIKeyNotFound
from openapi_server.models.retrieve_api_secret404_response import RetrieveAPISecret404Response
from openapi_server.models.retrieve_api_secrets200_response import RetrieveAPISecrets200Response
from openapi_server.models.retrieve_api_secrets401_response import RetrieveAPISecrets401Response
from openapi_server.models.revoke_api_secret403_response import RevokeAPISecret403Response
from openapi_server.models.secret_info import SecretInfo


pytestmark = pytest.mark.asyncio

async def test_create_api_secret(client):
    """Test case for create_api_secret

    Create API Secret
    """
    body = openapi_server.CreateSecretRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/accounts/{api_key}/secrets'.format(api_key='abcd1234'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_api_secret(client):
    """Test case for retrieve_api_secret

    Retrieve one API Secret
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{api_key}/secrets/{secret_id}'.format(api_key='abcd1234', secret_id='01234567-aaaa-bbbb-cccc-defdefdefdef'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_api_secrets(client):
    """Test case for retrieve_api_secrets

    Retrieve API Secrets
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{api_key}/secrets'.format(api_key='abcd1234'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_api_secret(client):
    """Test case for revoke_api_secret

    Revoke an API Secret
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/accounts/{api_key}/secrets/{secret_id}'.format(api_key='abcd1234', secret_id='01234567-aaaa-bbbb-cccc-defdefdefdef'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

