# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.insights_v1_video_room_summary_video_participant_summary import InsightsV1VideoRoomSummaryVideoParticipantSummary
from openapi_server.models.list_video_participant_summary_response import ListVideoParticipantSummaryResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_video_participant_summary(client):
    """Test case for fetch_video_participant_summary

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Video/Rooms/{room_sid}/Participants/{participant_sid}'.format(room_sid='room_sid_example', participant_sid='participant_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_video_participant_summary(client):
    """Test case for list_video_participant_summary

    
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
        path='/v1/Video/Rooms/{room_sid}/Participants'.format(room_sid='room_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

