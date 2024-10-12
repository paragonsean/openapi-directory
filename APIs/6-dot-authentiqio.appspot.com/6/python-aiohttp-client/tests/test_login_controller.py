# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.push_login_request200_response import PushLoginRequest200Response
from openapi_server.models.push_token import PushToken


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_push_login_request(client):
    """Test case for push_login_request

    
    """
    body = openapi_server.PushToken()
    params = [('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/jwt',
    }
    response = await client.request(
        method='POST',
        path='/login',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

