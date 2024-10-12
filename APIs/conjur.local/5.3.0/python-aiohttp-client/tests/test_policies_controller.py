# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.replace_policy201_response import ReplacePolicy201Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_load_policy(client):
    """Test case for load_policy

    Adds data to the existing Conjur policy.
    """
    body = None
    headers = { 
        'Content-Type': 'application/x-yaml',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/policies/{account}/policy/{identifier}'.format(account='account_example', identifier='root'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_replace_policy(client):
    """Test case for replace_policy

    Loads or replaces a Conjur policy document.
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-yaml',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/policies/{account}/policy/{identifier}'.format(account='account_example', identifier='root'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_policy(client):
    """Test case for update_policy

    Modifies an existing Conjur policy.
    """
    body = None
    headers = { 
        'Content-Type': 'application/x-yaml',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/policies/{account}/policy/{identifier}'.format(account='account_example', identifier='root'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

