# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_room_recording_response import ListRoomRecordingResponse
from openapi_server.models.room_recording_enum_status import RoomRecordingEnumStatus
from openapi_server.models.video_v1_room_room_recording import VideoV1RoomRoomRecording


pytestmark = pytest.mark.asyncio

async def test_delete_room_recording(client):
    """Test case for delete_room_recording

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Rooms/{room_sid}/Recordings/{sid}'.format(room_sid='room_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_room_recording(client):
    """Test case for fetch_room_recording

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Rooms/{room_sid}/Recordings/{sid}'.format(room_sid='room_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_room_recording(client):
    """Test case for list_room_recording

    
    """
    params = [('Status', openapi_server.RoomRecordingEnumStatus()),
                    ('SourceSid', 'source_sid_example'),
                    ('DateCreatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('DateCreatedBefore', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Rooms/{room_sid}/Recordings'.format(room_sid='room_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

