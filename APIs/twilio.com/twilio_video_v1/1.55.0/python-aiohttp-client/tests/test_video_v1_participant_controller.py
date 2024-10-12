# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_room_participant_response import ListRoomParticipantResponse
from openapi_server.models.room_participant_enum_status import RoomParticipantEnumStatus
from openapi_server.models.video_v1_room_room_participant import VideoV1RoomRoomParticipant


pytestmark = pytest.mark.asyncio

async def test_fetch_room_participant(client):
    """Test case for fetch_room_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Rooms/{room_sid}/Participants/{sid}'.format(room_sid='room_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_room_participant(client):
    """Test case for list_room_participant

    
    """
    params = [('Status', openapi_server.RoomParticipantEnumStatus()),
                    ('Identity', 'identity_example'),
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
        path='/v1/Rooms/{room_sid}/Participants'.format(room_sid='room_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_room_participant(client):
    """Test case for update_room_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'status': openapi_server.RoomParticipantEnumStatus()
        }
    response = await client.request(
        method='POST',
        path='/v1/Rooms/{room_sid}/Participants/{sid}'.format(room_sid='room_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

