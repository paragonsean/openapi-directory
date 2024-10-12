# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v1_shorten_post200_response import V1ShortenPost200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_shorten_post(client):
    """Test case for v1_shorten_post

    Create short link
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'url': 'url_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v1/shorten',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

