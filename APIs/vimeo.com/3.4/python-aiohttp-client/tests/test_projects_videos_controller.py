# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_add_video_to_project(client):
    """Test case for add_video_to_project

    Add a specific video to a project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{user_id}/projects/{project_id}/videos/{video_id}'.format(project_id=12345, user_id=152184, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_video_to_project_alt1(client):
    """Test case for add_video_to_project_alt1

    Add a specific video to a project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/me/projects/{project_id}/videos/{video_id}'.format(project_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_videos_to_project(client):
    """Test case for add_videos_to_project

    Add a list of videos to a project
    """
    params = [('uris', '/videos/258684937,/videos/273576296')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{user_id}/projects/{project_id}/videos'.format(project_id=12345, user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_videos_to_project_alt1(client):
    """Test case for add_videos_to_project_alt1

    Add a list of videos to a project
    """
    params = [('uris', '/videos/258684937,/videos/273576296')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/me/projects/{project_id}/videos'.format(project_id=12345),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_videos(client):
    """Test case for get_project_videos

    Get all the videos in a project
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/projects/{project_id}/videos'.format(project_id=12345, user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_videos_alt1(client):
    """Test case for get_project_videos_alt1

    Get all the videos in a project
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/projects/{project_id}/videos'.format(project_id=12345),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_video_from_project(client):
    """Test case for remove_video_from_project

    Remove a specific video from a project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/projects/{project_id}/videos/{video_id}'.format(project_id=12345, user_id=152184, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_video_from_project_alt1(client):
    """Test case for remove_video_from_project_alt1

    Remove a specific video from a project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/me/projects/{project_id}/videos/{video_id}'.format(project_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_videos_from_project(client):
    """Test case for remove_videos_from_project

    Remove a list of videos from a project
    """
    params = [('should_delete_clips', false),
                    ('uris', '/videos/258684937,/videos/273576296')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/projects/{project_id}/videos'.format(project_id=12345, user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_videos_from_project_alt1(client):
    """Test case for remove_videos_from_project_alt1

    Remove a list of videos from a project
    """
    params = [('should_delete_clips', false),
                    ('uris', '/videos/258684937,/videos/273576296')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/me/projects/{project_id}/videos'.format(project_id=12345),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

