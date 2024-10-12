# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.not_found import NotFound
from openapi_server.models.video import Video
from openapi_server.models.video_create_payload import VideoCreatePayload
from openapi_server.models.video_thumbnail_pick_payload import VideoThumbnailPickPayload
from openapi_server.models.video_update_payload import VideoUpdatePayload
from openapi_server.models.videos_list_response import VideosListResponse
from openapi_server.models.videostatus import Videostatus


pytestmark = pytest.mark.asyncio

async def test_d_elete_video(client):
    """Test case for d_elete_video

    Delete a video
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Jfrgz'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_video(client):
    """Test case for g_et_video

    Show a video
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}'.format(video_id='video_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_video_status(client):
    """Test case for g_et_video_status

    Show video status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/status'.format(video_id='vi4k0jvEUuaTdRAEjQ4Jfrgz'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_l_ist_videos(client):
    """Test case for l_ist_videos

    List all videos
    """
    params = [('title', 'My Video.mp4'),
                    ('tags', ['\"tags\": [\"captions\", \"dialogue\"]']),
                    ('metadata', ['[{\"key\":\"Author\", \"value\":\"John Doe\"}, {\"key\":\"Format\", \"value\":\"Tutorial\"}]']),
                    ('description', 'New Zealand'),
                    ('liveStreamId', 'li400mYKSgQ6xs7taUeSaEKr'),
                    ('sortBy', 'publishedAt'),
                    ('sortOrder', 'asc'),
                    ('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_atch_video(client):
    """Test case for p_atch_video

    Update a video
    """
    body = openapi_server.VideoUpdatePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/videos/{video_id}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Jfrgz'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_atch_videos_video_id_thumbnail(client):
    """Test case for p_atch_videos_video_id_thumbnail

    Pick a thumbnail
    """
    body = openapi_server.VideoThumbnailPickPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/videos/{video_id}/thumbnail'.format(video_id='vi4k0jvEUuaTdRAEjQ4Jfrgz'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ost_video(client):
    """Test case for p_ost_video

    Create a video
    """
    body = openapi_server.VideoCreatePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/videos',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_p_ost_videos_video_id_source(client):
    """Test case for p_ost_videos_video_id_source

    Upload a video
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'content_range': 'Content-Range: bytes 200-100/5000',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/videos/{video_id}/source'.format(video_id='vi4k0jvEUuaTdRAEjQ4Jfrgz'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_p_ost_videos_video_id_thumbnail(client):
    """Test case for p_ost_videos_video_id_thumbnail

    Upload a thumbnail
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/videos/{video_id}/thumbnail'.format(video_id='video_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

