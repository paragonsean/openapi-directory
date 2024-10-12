# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_token200_response import PostToken200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.post_token_request import PostTokenRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_token(client):
    """Test case for post_token

    Get authentication token
    """
    body = openapi_server.PostTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/api/oauth/v1/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

