# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authentication_token_response import AuthenticationTokenResponse


pytestmark = pytest.mark.asyncio

async def test_auth_post(client):
    """Test case for auth_post

    
    """
    params = [('client_id', 'client_id_example'),
                    ('client_secret', 'client_secret_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/auth',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

