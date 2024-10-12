# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_videos_to_channel_request import AddVideosToChannelRequest
from openapi_server.models.channel import Channel
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.remove_videos_from_channel_request import RemoveVideosFromChannelRequest
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_add_video_to_channel(client):
    """Test case for add_video_to_channel

    Add a specific video to a channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/videos/{video_id}'.format(channel_id=927, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_videos_to_channel(client):
    """Test case for add_videos_to_channel

    Add a list of videos to a channel
    """
    body = openapi_server.AddVideosToChannelRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/channels/{channel_id}/videos'.format(channel_id=927),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_from_channel(client):
    """Test case for delete_video_from_channel

    Remove a specific video from a channel
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_id}/videos/{video_id}'.format(channel_id=927, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_available_video_channels(client):
    """Test case for get_available_video_channels

    Get all the channels to which a user can add or remove a specific video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.channel+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/available_channels'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_video(client):
    """Test case for get_channel_video

    Get a specific video in a channel
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/videos/{video_id}'.format(channel_id=927, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_videos(client):
    """Test case for get_channel_videos

    Get all the videos in a channel
    """
    params = [('containing_uri', '/videos/258684937'),
                    ('direction', 'asc'),
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
        path='/channels/{channel_id}/videos'.format(channel_id=927),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_videos_from_channel(client):
    """Test case for remove_videos_from_channel

    Remove a list of videos from a channel
    """
    body = openapi_server.RemoveVideosFromChannelRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{channel_id}/videos'.format(channel_id=927),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

