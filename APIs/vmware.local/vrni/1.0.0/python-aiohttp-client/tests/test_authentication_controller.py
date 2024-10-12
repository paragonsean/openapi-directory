# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.token import Token
from openapi_server.models.user_credential import UserCredential


pytestmark = pytest.mark.asyncio

async def test_create(client):
    """Test case for create

    Create an auth token
    """
    body = {"password":"password","domain":{"domain_type":"LDAP","value":"example.com"},"username":"admin@vrni.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete(client):
    """Test case for delete

    Delete an auth token.
    """
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/auth/token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

