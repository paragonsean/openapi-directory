# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.currently_playing_context_object import CurrentlyPlayingContextObject
from openapi_server.models.cursor_paging_play_history_object import CursorPagingPlayHistoryObject
from openapi_server.models.get_a_users_available_devices200_response import GetAUsersAvailableDevices200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.queue_object import QueueObject
from openapi_server.models.start_a_users_playback_request import StartAUsersPlaybackRequest
from openapi_server.models.transfer_a_users_playback_request import TransferAUsersPlaybackRequest


pytestmark = pytest.mark.asyncio

async def test_add_to_queue(client):
    """Test case for add_to_queue

    Add Item to Playback Queue 
    """
    params = [('uri', 'spotify:track:4iV5W9uYEdYUVa79Axb7Rh'),
                    ('device_id', '0d1841b0976bae2a3a310dd74c0f3df354899bc8')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/me/player/queue',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_users_available_devices(client):
    """Test case for get_a_users_available_devices

    Get Available Devices 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/player/devices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_information_about_the_users_current_playback(client):
    """Test case for get_information_about_the_users_current_playback

    Get Playback State 
    """
    params = [('market', 'ES'),
                    ('additional_types', 'additional_types_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/player',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_queue(client):
    """Test case for get_queue

    Get the User's Queue 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/player/queue',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recently_played(client):
    """Test case for get_recently_played

    Get Recently Played Tracks 
    """
    params = [('limit', 20),
                    ('after', 1484811043508),
                    ('before', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/player/recently-played',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_the_users_currently_playing_track(client):
    """Test case for get_the_users_currently_playing_track

    Get Currently Playing Track 
    """
    params = [('market', 'ES'),
                    ('additional_types', 'additional_types_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/player/currently-playing',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pause_a_users_playback(client):
    """Test case for pause_a_users_playback

    Pause Playback 
    """
    params = [('device_id', '0d1841b0976bae2a3a310dd74c0f3df354899bc8')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/player/pause',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seek_to_position_in_currently_playing_track(client):
    """Test case for seek_to_position_in_currently_playing_track

    Seek To Position 
    """
    params = [('position_ms', 25000),
                    ('device_id', '0d1841b0976bae2a3a310dd74c0f3df354899bc8')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/player/seek',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_repeat_mode_on_users_playback(client):
    """Test case for set_repeat_mode_on_users_playback

    Set Repeat Mode 
    """
    params = [('state', 'context'),
                    ('device_id', '0d1841b0976bae2a3a310dd74c0f3df354899bc8')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/player/repeat',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_volume_for_users_playback(client):
    """Test case for set_volume_for_users_playback

    Set Playback Volume 
    """
    params = [('volume_percent', 50),
                    ('device_id', '0d1841b0976bae2a3a310dd74c0f3df354899bc8')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/player/volume',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skip_users_playback_to_next_track(client):
    """Test case for skip_users_playback_to_next_track

    Skip To Next 
    """
    params = [('device_id', '0d1841b0976bae2a3a310dd74c0f3df354899bc8')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/me/player/next',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_skip_users_playback_to_previous_track(client):
    """Test case for skip_users_playback_to_previous_track

    Skip To Previous 
    """
    params = [('device_id', '0d1841b0976bae2a3a310dd74c0f3df354899bc8')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/me/player/previous',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_a_users_playback(client):
    """Test case for start_a_users_playback

    Start/Resume Playback 
    """
    body = openapi_server.StartAUsersPlaybackRequest()
    params = [('device_id', '0d1841b0976bae2a3a310dd74c0f3df354899bc8')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/player/play',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_shuffle_for_users_playback(client):
    """Test case for toggle_shuffle_for_users_playback

    Toggle Playback Shuffle 
    """
    params = [('state', true),
                    ('device_id', '0d1841b0976bae2a3a310dd74c0f3df354899bc8')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/player/shuffle',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transfer_a_users_playback(client):
    """Test case for transfer_a_users_playback

    Transfer Playback 
    """
    body = openapi_server.TransferAUsersPlaybackRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/player',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

