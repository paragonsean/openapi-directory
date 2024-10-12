# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.buffer_request_dto import BufferRequestDto
from openapi_server.models.group_info_dto import GroupInfoDto
from openapi_server.models.ignore_wait_request_dto import IgnoreWaitRequestDto
from openapi_server.models.join_group_request_dto import JoinGroupRequestDto
from openapi_server.models.move_playlist_item_request_dto import MovePlaylistItemRequestDto
from openapi_server.models.new_group_request_dto import NewGroupRequestDto
from openapi_server.models.next_item_request_dto import NextItemRequestDto
from openapi_server.models.ping_request_dto import PingRequestDto
from openapi_server.models.play_request_dto import PlayRequestDto
from openapi_server.models.previous_item_request_dto import PreviousItemRequestDto
from openapi_server.models.queue_request_dto import QueueRequestDto
from openapi_server.models.ready_request_dto import ReadyRequestDto
from openapi_server.models.remove_from_playlist_request_dto import RemoveFromPlaylistRequestDto
from openapi_server.models.seek_request_dto import SeekRequestDto
from openapi_server.models.set_playlist_item_request_dto import SetPlaylistItemRequestDto
from openapi_server.models.set_repeat_mode_request_dto import SetRepeatModeRequestDto
from openapi_server.models.set_shuffle_mode_request_dto import SetShuffleModeRequestDto


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_buffering(client):
    """Test case for sync_play_buffering

    Notify SyncPlay group that member is buffering.
    """
    body = {"When":"2000-01-23T04:56:07.000+00:00","PositionTicks":0,"PlaylistItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","IsPlaying":True}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Buffering',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_create_group(client):
    """Test case for sync_play_create_group

    Create a new SyncPlay group.
    """
    body = {"GroupName":"GroupName"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/New',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_play_get_groups(client):
    """Test case for sync_play_get_groups

    Gets all SyncPlay groups.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/SyncPlay/List',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_join_group(client):
    """Test case for sync_play_join_group

    Join an existing SyncPlay group.
    """
    body = {"GroupId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Join',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_play_leave_group(client):
    """Test case for sync_play_leave_group

    Leave the joined SyncPlay group.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Leave',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_move_playlist_item(client):
    """Test case for sync_play_move_playlist_item

    Request to move an item in the playlist in SyncPlay group.
    """
    body = {"PlaylistItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","NewIndex":0}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/MovePlaylistItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_next_item(client):
    """Test case for sync_play_next_item

    Request next item in SyncPlay group.
    """
    body = {"PlaylistItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/NextItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_play_pause(client):
    """Test case for sync_play_pause

    Request pause in SyncPlay group.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Pause',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_ping(client):
    """Test case for sync_play_ping

    Update session ping.
    """
    body = {"Ping":0}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Ping',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_previous_item(client):
    """Test case for sync_play_previous_item

    Request previous item in SyncPlay group.
    """
    body = {"PlaylistItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/PreviousItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_queue(client):
    """Test case for sync_play_queue

    Request to queue items to the playlist of a SyncPlay group.
    """
    body = {"Mode":"Queue","ItemIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Queue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_ready(client):
    """Test case for sync_play_ready

    Notify SyncPlay group that member is ready for playback.
    """
    body = {"When":"2000-01-23T04:56:07.000+00:00","PositionTicks":0,"PlaylistItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","IsPlaying":True}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Ready',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_remove_from_playlist(client):
    """Test case for sync_play_remove_from_playlist

    Request to remove items from the playlist in SyncPlay group.
    """
    body = {"PlaylistItemIds":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/RemoveFromPlaylist',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_seek(client):
    """Test case for sync_play_seek

    Request seek in SyncPlay group.
    """
    body = {"PositionTicks":0}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Seek',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_set_ignore_wait(client):
    """Test case for sync_play_set_ignore_wait

    Request SyncPlay group to ignore member during group-wait.
    """
    body = {"IgnoreWait":True}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/SetIgnoreWait',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_set_new_queue(client):
    """Test case for sync_play_set_new_queue

    Request to set new playlist in SyncPlay group.
    """
    body = {"PlayingQueue":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"StartPositionTicks":6,"PlayingItemPosition":0}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/SetNewQueue',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_set_playlist_item(client):
    """Test case for sync_play_set_playlist_item

    Request to change playlist item in SyncPlay group.
    """
    body = {"PlaylistItemId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/SetPlaylistItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_set_repeat_mode(client):
    """Test case for sync_play_set_repeat_mode

    Request to set repeat mode in SyncPlay group.
    """
    body = {"Mode":"RepeatOne"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/SetRepeatMode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sync_play_set_shuffle_mode(client):
    """Test case for sync_play_set_shuffle_mode

    Request to set shuffle mode in SyncPlay group.
    """
    body = {"Mode":"Sorted"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/SetShuffleMode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_play_stop(client):
    """Test case for sync_play_stop

    Request stop in SyncPlay group.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Stop',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sync_play_unpause(client):
    """Test case for sync_play_unpause

    Request unpause in SyncPlay group.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/SyncPlay/Unpause',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

