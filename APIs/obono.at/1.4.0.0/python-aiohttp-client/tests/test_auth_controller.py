# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_result import AuthResult


pytestmark = pytest.mark.asyncio

async def test_auth_get(client):
    """Test case for auth_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/auth',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

