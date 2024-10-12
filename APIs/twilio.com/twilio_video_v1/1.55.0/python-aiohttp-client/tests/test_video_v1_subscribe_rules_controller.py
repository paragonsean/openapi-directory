# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.video_v1_room_room_participant_room_participant_subscribe_rule import VideoV1RoomRoomParticipantRoomParticipantSubscribeRule


pytestmark = pytest.mark.asyncio

async def test_fetch_room_participant_subscribe_rule(client):
    """Test case for fetch_room_participant_subscribe_rule

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules'.format(room_sid='room_sid_example', participant_sid='participant_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_room_participant_subscribe_rule(client):
    """Test case for update_room_participant_subscribe_rule

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'rules': None
        }
    response = await client.request(
        method='POST',
        path='/v1/Rooms/{room_sid}/Participants/{participant_sid}/SubscribeRules'.format(room_sid='room_sid_example', participant_sid='participant_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

