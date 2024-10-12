# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.token import Token
from openapi_server.models.token_error import TokenError
from openapi_server.models.token_request import TokenRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_access_token(client):
    """Test case for get_access_token

    Retrieve an access token
    """
    body = {"refresh_token":"refresh_token","password":"password","grant_type":"grant_type","user_id":0,"scope":"scope","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

