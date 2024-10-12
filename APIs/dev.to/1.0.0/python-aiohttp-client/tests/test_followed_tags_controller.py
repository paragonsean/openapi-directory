# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.followed_tag import FollowedTag


pytestmark = pytest.mark.asyncio

async def test_get_followed_tags(client):
    """Test case for get_followed_tags

    Followed Tags
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/follows/tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

