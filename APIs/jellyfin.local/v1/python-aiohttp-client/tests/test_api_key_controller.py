# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authentication_info_query_result import AuthenticationInfoQueryResult


pytestmark = pytest.mark.asyncio

async def test_create_key(client):
    """Test case for create_key

    Create a new api key.
    """
    params = [('app', 'app_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Auth/Keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_keys(client):
    """Test case for get_keys

    Get all keys.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Auth/Keys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_key(client):
    """Test case for revoke_key

    Remove an api key.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Auth/Keys/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

