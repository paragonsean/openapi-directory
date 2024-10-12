# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_add_video_to_group(client):
    """Test case for add_video_to_group

    Add a video to a group
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/groups/{group_id}/videos/{video_id}'.format(group_id=1108, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_from_group(client):
    """Test case for delete_video_from_group

    Remove a video from a group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}/videos/{video_id}'.format(group_id=1108, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_video(client):
    """Test case for get_group_video

    Get a specific video in a group
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}/videos/{video_id}'.format(group_id=1108, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_videos(client):
    """Test case for get_group_videos

    Get all the videos in a group
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
        path='/groups/{group_id}/videos'.format(group_id=1108),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

