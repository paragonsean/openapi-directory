# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cache_post_request import CachePostRequest
from openapi_server.models.problem_detail import ProblemDetail


pytestmark = pytest.mark.asyncio

async def test_cache_nonce_get(client):
    """Test case for cache_nonce_get

    Cache: Get Subdocument
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/story/cache/{nonce}'.format(nonce='nonce_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cache_post(client):
    """Test case for cache_post

    Cache: Store Subdocument
    """
    body = openapi_server.CachePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/story/cache',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

