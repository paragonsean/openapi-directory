# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.authentication import Authentication


pytestmark = pytest.mark.asyncio

async def test_authenticate(client):
    """Test case for authenticate

    Authenticate with the API.
    """
    body = openapi_server.Authentication()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/apps/accesstokens',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

