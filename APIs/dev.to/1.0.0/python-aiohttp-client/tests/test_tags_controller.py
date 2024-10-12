# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.followed_tag import FollowedTag
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_get_followed_tags_0(client):
    """Test case for get_followed_tags_0

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


pytestmark = pytest.mark.asyncio

async def test_get_tags(client):
    """Test case for get_tags

    Tags
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

