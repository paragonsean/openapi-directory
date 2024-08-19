# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.token_request import TokenRequest
from openapi_server.models.token_response import TokenResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_scripts_tokenization_tokens_post(client):
    """Test case for scripts_tokenization_tokens_post

    Tokenize credit card
    """
    token_request = openapi_server.TokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/scripts/tokenization/tokens',
        headers=headers,
        json=token_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

