# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_room_participant_subscribed_track_response import ListRoomParticipantSubscribedTrackResponse
from openapi_server.models.video_v1_room_room_participant_room_participant_subscribed_track import VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack


pytestmark = pytest.mark.asyncio

async def test_fetch_room_participant_subscribed_track(client):
    """Test case for fetch_room_participant_subscribed_track

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks/{sid}'.format(room_sid='room_sid_example', participant_sid='participant_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_room_participant_subscribed_track(client):
    """Test case for list_room_participant_subscribed_track

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribedTracks'.format(room_sid='room_sid_example', participant_sid='participant_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

