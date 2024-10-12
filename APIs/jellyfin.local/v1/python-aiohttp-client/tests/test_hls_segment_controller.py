# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_hls_audio_segment_legacy_aac(client):
    """Test case for get_hls_audio_segment_legacy_aac

    Gets the specified audio segment for an audio item.
    """
    headers = { 
        'Accept': 'audio/*',
    }
    response = await client.request(
        method='GET',
        path='/Audio/{item_id}/hls/{segment_id}/stream.aac'.format(item_id='item_id_example', segment_id='segment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hls_audio_segment_legacy_mp3(client):
    """Test case for get_hls_audio_segment_legacy_mp3

    Gets the specified audio segment for an audio item.
    """
    headers = { 
        'Accept': 'audio/*',
    }
    response = await client.request(
        method='GET',
        path='/Audio/{item_id}/hls/{segment_id}/stream.mp3'.format(item_id='item_id_example', segment_id='segment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hls_playlist_legacy(client):
    """Test case for get_hls_playlist_legacy

    Gets a hls video playlist.
    """
    headers = { 
        'Accept': 'application/x-mpegURL',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Videos/{item_id}/hls/{playlist_id}/stream.m3u8'.format(item_id='item_id_example', playlist_id='playlist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_hls_video_segment_legacy(client):
    """Test case for get_hls_video_segment_legacy

    Gets a hls video segment.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Videos/{item_id}/hls/{playlist_id}/{segment_id_segment_container}'.format(item_id='item_id_example', playlist_id='playlist_id_example', segment_id='segment_id_example', segment_container='segment_container_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_encoding_process(client):
    """Test case for stop_encoding_process

    Stops an active encoding.
    """
    params = [('deviceId', 'device_id_example'),
                    ('playSessionId', 'play_session_id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Videos/ActiveEncodings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

