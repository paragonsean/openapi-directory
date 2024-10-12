# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.insights_v1_video_room_summary import InsightsV1VideoRoomSummary
from openapi_server.models.list_video_room_summary_response import ListVideoRoomSummaryResponse
from openapi_server.models.video_room_summary_enum_codec import VideoRoomSummaryEnumCodec
from openapi_server.models.video_room_summary_enum_room_type import VideoRoomSummaryEnumRoomType


pytestmark = pytest.mark.asyncio

async def test_fetch_video_room_summary(client):
    """Test case for fetch_video_room_summary

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Video/Rooms/{room_sid}'.format(room_sid='room_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_video_room_summary(client):
    """Test case for list_video_room_summary

    
    """
    params = [('RoomType', [openapi_server.VideoRoomSummaryEnumRoomType()]),
                    ('Codec', [openapi_server.VideoRoomSummaryEnumCodec()]),
                    ('RoomName', 'room_name_example'),
                    ('CreatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('CreatedBefore', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Video/Rooms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

