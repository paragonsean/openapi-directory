# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.raw_statistics_list_live_stream_analytics_response import RawStatisticsListLiveStreamAnalyticsResponse
from openapi_server.models.raw_statistics_list_player_session_events_response import RawStatisticsListPlayerSessionEventsResponse
from openapi_server.models.raw_statistics_list_sessions_response import RawStatisticsListSessionsResponse


pytestmark = pytest.mark.asyncio

async def test_g_et_analytics_live_streams_live_stream_id(client):
    """Test case for g_et_analytics_live_streams_live_stream_id

    List live stream player sessions
    """
    params = [('period', '2019-01-01'),
                    ('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/analytics/live-streams/{live_stream_id}'.format(live_stream_id='vi4k0jvEUuaTdRAEjQ4Jfrgz'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_analytics_sessions_session_id_events(client):
    """Test case for g_et_analytics_sessions_session_id_events

    List player session events
    """
    params = [('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/analytics/sessions/{session_id}/events'.format(session_id='psEmFwGQUAXR2lFHj5nDOpy'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_analytics_videos_video_id(client):
    """Test case for g_et_analytics_videos_video_id

    List video player sessions
    """
    params = [('period', 'period_example'),
                    ('metadata', ['[{\"key\": \"Author\", \"value\": \"John Doe\"}, {\"key\": \"Format\", \"value\": \"Tutorial\"}]']),
                    ('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/analytics/videos/{video_id}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Prklg'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

