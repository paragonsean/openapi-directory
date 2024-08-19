# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_video_views_response import ListVideoViewsResponse
from openapi_server.models.video_view_response import VideoViewResponse


pytestmark = pytest.mark.asyncio

async def test_get_video_view(client):
    """Test case for get_video_view

    Get a Video View
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/video-views/{video_view_id}'.format(video_view_id='abcd1234'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_video_views(client):
    """Test case for list_video_views

    List Video Views
    """
    params = [('limit', 25),
                    ('page', 1),
                    ('viewer_id', 'viewer_id_example'),
                    ('error_id', 56),
                    ('order_direction', 'order_direction_example'),
                    ('filters[]', ['filters_example']),
                    ('timeframe[]', ['timeframe_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/video-views',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

