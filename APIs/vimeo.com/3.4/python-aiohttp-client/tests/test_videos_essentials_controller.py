# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit_video_request import EditVideoRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_check_if_user_owns_video(client):
    """Test case for check_if_user_owns_video

    Check if a user owns a video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/videos/{video_id}'.format(user_id=152184, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_if_user_owns_video_alt1(client):
    """Test case for check_if_user_owns_video_alt1

    Check if a user owns a video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/videos/{video_id}'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video(client):
    """Test case for delete_video

    Delete a video
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_video(client):
    """Test case for edit_video

    Edit a video
    """
    body = openapi_server.EditVideoRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Content-Type': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/videos/{video_id}'.format(video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_appearances(client):
    """Test case for get_appearances

    Get all the videos in which a user appears
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
        path='/users/{user_id}/appearances'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_appearances_alt1(client):
    """Test case for get_appearances_alt1

    Get all the videos in which a user appears
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
        path='/me/appearances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video(client):
    """Test case for get_video

    Get a specific video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_videos(client):
    """Test case for get_videos

    Get all the videos that a user has uploaded
    """
    params = [('containing_uri', '/videos/258684937'),
                    ('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('filter_embeddable', true),
                    ('filter_playable', true),
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
        path='/users/{user_id}/videos'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_videos_alt1(client):
    """Test case for get_videos_alt1

    Get all the videos that a user has uploaded
    """
    params = [('containing_uri', '/videos/258684937'),
                    ('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('filter_embeddable', true),
                    ('filter_playable', true),
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
        path='/me/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_videos(client):
    """Test case for search_videos

    Search for videos
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('links', 'https://vimeo.com/122375452,https://vimeo.com/273576296'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'staff picks'),
                    ('sort', 'sort_example'),
                    ('uris', '/videos/122375452,/videos/273576296')]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

