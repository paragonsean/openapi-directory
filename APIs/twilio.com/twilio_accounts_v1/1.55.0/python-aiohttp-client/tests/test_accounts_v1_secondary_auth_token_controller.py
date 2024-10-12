# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_v1_secondary_auth_token import AccountsV1SecondaryAuthToken


pytestmark = pytest.mark.asyncio

async def test_create_secondary_auth_token(client):
    """Test case for create_secondary_auth_token

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/AuthTokens/Secondary',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_secondary_auth_token(client):
    """Test case for delete_secondary_auth_token

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/AuthTokens/Secondary',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

