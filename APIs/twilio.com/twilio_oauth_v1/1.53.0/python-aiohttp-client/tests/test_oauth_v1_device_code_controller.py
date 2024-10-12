# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.oauth_v1_device_code import OauthV1DeviceCode


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_device_code(client):
    """Test case for create_device_code

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'audiences': ['audiences_example'],
        'client_sid': 'client_sid_example',
        'scopes': ['scopes_example']
        }
    response = await client.request(
        method='POST',
        path='/v1/device/code',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

