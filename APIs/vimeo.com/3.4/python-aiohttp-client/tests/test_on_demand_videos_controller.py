# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_video_to_vod_request import AddVideoToVodRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_video import OnDemandVideo
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_add_video_to_vod(client):
    """Test case for add_video_to_vod

    Add a video to an On Demand page
    """
    body = openapi_server.AddVideoToVodRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.video+json',
        'Content-Type': 'application/vnd.vimeo.ondemand.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/ondemand/pages/{ondemand_id}/videos/{video_id}'.format(ondemand_id=61326, video_id=12345),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_from_vod(client):
    """Test case for delete_video_from_vod

    Remove a video from an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/ondemand/pages/{ondemand_id}/videos/{video_id}'.format(ondemand_id=61326, video_id=12345),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_video(client):
    """Test case for get_vod_video

    Get a specific video on an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/videos/{video_id}'.format(ondemand_id=61326, video_id=12345),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_videos(client):
    """Test case for get_vod_videos

    Get all the videos on an On Demand page
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/videos'.format(ondemand_id=61326),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

