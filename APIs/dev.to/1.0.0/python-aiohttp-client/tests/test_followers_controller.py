# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_followers200_response_inner import GetFollowers200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_followers(client):
    """Test case for get_followers

    Followers
    """
    params = [('page', 1),
                    ('per_page', 30),
                    ('sort', 'created_at')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/followers/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

