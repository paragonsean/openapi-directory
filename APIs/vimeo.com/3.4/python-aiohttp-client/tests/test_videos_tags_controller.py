# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_video_tags_request import AddVideoTagsRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.tag import Tag
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_add_video_tag(client):
    """Test case for add_video_tag

    Add a specific tag to a video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/videos/{video_id}/tags/{word}'.format(video_id=258684937, word='awesome'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_video_tags(client):
    """Test case for add_video_tags

    Add a list of tags to a video
    """
    body = openapi_server.AddVideoTagsRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Content-Type': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/videos/{video_id}/tags'.format(video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_video_for_tag(client):
    """Test case for check_video_for_tag

    Check if a tag has been added to a video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/tags/{word}'.format(video_id=258684937, word='awesome'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_tag(client):
    """Test case for delete_video_tag

    Remove a tag from a video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}/tags/{word}'.format(video_id=258684937, word='awesome'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_tags(client):
    """Test case for get_video_tags

    Get all the tags of a video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.tag+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/tags'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_videos_with_tag(client):
    """Test case for get_videos_with_tag

    Get all the videos with a specific tag
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{word}/videos'.format(word='awesome'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

