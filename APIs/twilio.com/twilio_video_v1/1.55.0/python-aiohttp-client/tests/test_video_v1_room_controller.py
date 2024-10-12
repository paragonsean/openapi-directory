# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_room_response import ListRoomResponse
from openapi_server.models.room_enum_room_status import RoomEnumRoomStatus
from openapi_server.models.room_enum_room_type import RoomEnumRoomType
from openapi_server.models.room_enum_video_codec import RoomEnumVideoCodec
from openapi_server.models.video_v1_room import VideoV1Room


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_room(client):
    """Test case for create_room

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'audio_only': True,
        'empty_room_timeout': 56,
        'enable_turn': True,
        'large_room': True,
        'max_participant_duration': 56,
        'max_participants': 56,
        'media_region': 'media_region_example',
        'record_participants_on_connect': True,
        'recording_rules': None,
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'type': openapi_server.RoomEnumRoomType(),
        'unique_name': 'unique_name_example',
        'unused_room_timeout': 56,
        'video_codecs': [openapi_server.RoomEnumVideoCodec()]
        }
    response = await client.request(
        method='POST',
        path='/v1/Rooms',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_room(client):
    """Test case for fetch_room

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Rooms/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_room(client):
    """Test case for list_room

    
    """
    params = [('Status', openapi_server.RoomEnumRoomStatus()),
                    ('UniqueName', 'unique_name_example'),
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
        path='/v1/Rooms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_room(client):
    """Test case for update_room

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'status': openapi_server.RoomEnumRoomStatus()
        }
    response = await client.request(
        method='POST',
        path='/v1/Rooms/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

