# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_text_track_alt1_request import CreateTextTrackAlt1Request
from openapi_server.models.edit_text_track_request import EditTextTrackRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.text_track import TextTrack


pytestmark = pytest.mark.asyncio

async def test_create_text_track(client):
    """Test case for create_text_track

    Add a text track to a video
    """
    body = openapi_server.CreateTextTrackAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.video.texttrack+json',
        'Content-Type': 'application/vnd.vimeo.video.texttrack+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/videos/{video_id}/texttracks'.format(video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_text_track_alt1(client):
    """Test case for create_text_track_alt1

    Add a text track to a video
    """
    body = openapi_server.CreateTextTrackAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.video.texttrack+json',
        'Content-Type': 'application/vnd.vimeo.video.texttrack+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_id}/videos/{video_id}/texttracks'.format(channel_id=927, video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_text_track(client):
    """Test case for delete_text_track

    Delete a text track
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video.texttrack+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}/texttracks/{texttrack_id}'.format(texttrack_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_text_track(client):
    """Test case for edit_text_track

    Edit a text track
    """
    body = openapi_server.EditTextTrackRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.video.texttrack+json',
        'Content-Type': 'application/vnd.vimeo.video.texttrack+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/videos/{video_id}/texttracks/{texttrack_id}'.format(texttrack_id=12345, video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_track(client):
    """Test case for get_text_track

    Get a specific text track
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video.texttrack+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/texttracks/{texttrack_id}'.format(texttrack_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_tracks(client):
    """Test case for get_text_tracks

    Get all the text tracks of a video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video.texttrack+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/texttracks'.format(video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_tracks_alt1(client):
    """Test case for get_text_tracks_alt1

    Get all the text tracks of a video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.video.texttrack+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/videos/{video_id}/texttracks'.format(channel_id=927, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

