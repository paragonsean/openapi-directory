# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_delete_from_watch_history(client):
    """Test case for delete_from_watch_history

    Delete a specific video from a user's watch history
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/me/watched/videos/{video_id}'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_watch_history(client):
    """Test case for delete_watch_history

    Delete a user's watch history
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/me/watched/videos',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_watch_history(client):
    """Test case for get_watch_history

    Get all the videos that a user has watched
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/watched/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

