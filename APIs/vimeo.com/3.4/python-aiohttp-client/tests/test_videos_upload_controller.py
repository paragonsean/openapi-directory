# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.upload_attempt import UploadAttempt
from openapi_server.models.upload_video_alt1_request import UploadVideoAlt1Request
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_complete_streaming_upload(client):
    """Test case for complete_streaming_upload

    Complete a user's streaming upload
    """
    params = [('signature', 'cd89a20adde7a608f3331e71c37bdfa087bacbf3'),
                    ('video_file_id', 1234)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/uploads/{upload}'.format(upload=12345, user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upload_attempt(client):
    """Test case for get_upload_attempt

    Get a user's upload attempt
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.uploadattempt+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/uploads/{upload}'.format(upload=12345, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_video(client):
    """Test case for upload_video

    Upload a video
    """
    body = openapi_server.UploadVideoAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Content-Type': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/videos'.format(user_id=152184),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_video_alt1(client):
    """Test case for upload_video_alt1

    Upload a video
    """
    body = openapi_server.UploadVideoAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Content-Type': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/me/videos',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

