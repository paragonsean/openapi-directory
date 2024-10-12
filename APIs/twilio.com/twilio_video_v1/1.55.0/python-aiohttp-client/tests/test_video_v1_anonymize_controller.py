# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.video_v1_room_room_participant_room_participant_anonymize import VideoV1RoomRoomParticipantRoomParticipantAnonymize


pytestmark = pytest.mark.asyncio

async def test_update_room_participant_anonymize(client):
    """Test case for update_room_participant_anonymize

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/Rooms/{room_sid}/Participants/{sid}/Anonymize'.format(room_sid='room_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

