# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_create_secret(client):
    """Test case for create_secret

    Creates a secret value within the specified variable.
    """
    body = 'body_example'
    params = [('expirations', 'expirations_example')]
    headers = { 
        'Content-Type': 'application/octet-stream',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/secrets/{account}/{kind}/{identifier}'.format(account='account_example', kind='kind_example', identifier='identifier_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_secret(client):
    """Test case for get_secret

    Fetches the value of a secret from the specified Secret.
    """
    params = [('version', 56)]
    headers = { 
        'Accept': 'text/plain',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/secrets/{account}/{kind}/{identifier}'.format(account='account_example', kind='kind_example', identifier='identifier_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_secrets(client):
    """Test case for get_secrets

    Fetch multiple secrets
    """
    params = [('variable_ids', 'myorg:variable:secret1,myorg:variable:secret1')]
    headers = { 
        'Accept': 'application/json',
        'x_request_id': 'test-id',
        'accept_encoding': 'accept_encoding_example',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/secrets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

