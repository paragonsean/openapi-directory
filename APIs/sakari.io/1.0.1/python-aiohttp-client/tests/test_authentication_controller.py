# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.token_request import TokenRequest
from openapi_server.models.token_response import TokenResponse


pytestmark = pytest.mark.asyncio

async def test_auth_token(client):
    """Test case for auth_token

    Get token for accessing APIs
    """
    body = {"grant_type":"client_credentials","client_secret":"00000000-0000-0000-0000-00000000000","client_id":"00000000-0000-0000-0000-00000000000"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/oauth2/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

