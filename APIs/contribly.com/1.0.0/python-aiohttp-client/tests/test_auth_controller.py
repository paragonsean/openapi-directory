# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authority import Authority
from openapi_server.models.credential import Credential


pytestmark = pytest.mark.asyncio

async def test_credentials_get(client):
    """Test case for credentials_get

    List the credentials associated with the authenticated user.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/credentials',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scopes_get(client):
    """Test case for scopes_get

    Scopes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/scopes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_post(client):
    """Test case for verify_post

    Verify token and return details of the owning user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/verify',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

