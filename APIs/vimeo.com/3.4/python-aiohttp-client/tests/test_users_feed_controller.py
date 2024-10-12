# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity31 import Activity31


pytestmark = pytest.mark.asyncio

async def test_get_feed(client):
    """Test case for get_feed

    Get all videos in a user's feed
    """
    params = [('offset', '280'),
                    ('page', 1),
                    ('per_page', 10),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.activity+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/feed'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_feed_alt1(client):
    """Test case for get_feed_alt1

    Get all videos in a user's feed
    """
    params = [('offset', '280'),
                    ('page', 1),
                    ('per_page', 10),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.activity+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/feed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

