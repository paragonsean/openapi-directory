# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.redirect import Redirect
from openapi_server.models.tokens_get_ephemeral_token_response_body_yaml import TokensGetEphemeralTokenResponseBodyYaml


pytestmark = pytest.mark.asyncio

async def test_tokens_get_ephemeral_token(client):
    """Test case for tokens_get_ephemeral_token

    Get Ephemeral Token
    """
    params = [('redirect', openapi_server.Redirect())]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/tokens/ephemeral',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

