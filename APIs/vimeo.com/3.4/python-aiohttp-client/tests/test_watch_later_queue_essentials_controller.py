# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_add_video_to_watch_later(client):
    """Test case for add_video_to_watch_later

    Add a video to a user's Watch Later queue
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{user_id}/watchlater/{video_id}'.format(user_id=152184, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_video_to_watch_later_alt1(client):
    """Test case for add_video_to_watch_later_alt1

    Add a video to a user's Watch Later queue
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/me/watchlater/{video_id}'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_watch_later_queue(client):
    """Test case for check_watch_later_queue

    Check if a user has added a specific video to their Watch Later queue
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/watchlater/{video_id}'.format(user_id=152184, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_watch_later_queue_alt1(client):
    """Test case for check_watch_later_queue_alt1

    Check if a user has added a specific video to their Watch Later queue
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/watchlater/{video_id}'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_from_watch_later(client):
    """Test case for delete_video_from_watch_later

    Remove a video from a user's Watch Later queue
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/watchlater/{video_id}'.format(user_id=152184, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_from_watch_later_alt1(client):
    """Test case for delete_video_from_watch_later_alt1

    Remove a video from a user's Watch Later queue
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/me/watchlater/{video_id}'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_watch_later_queue(client):
    """Test case for get_watch_later_queue

    Get all the videos in a user's Watch Later queue
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('filter_embeddable', true),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/watchlater'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_watch_later_queue_alt1(client):
    """Test case for get_watch_later_queue_alt1

    Get all the videos in a user's Watch Later queue
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('filter_embeddable', true),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/watchlater',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

