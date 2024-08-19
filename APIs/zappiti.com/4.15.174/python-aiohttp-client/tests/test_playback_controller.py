# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.last_media_request import LastMediaRequest
from openapi_server.models.last_media_result import LastMediaResult
from openapi_server.models.start_video_request import StartVideoRequest
from openapi_server.models.start_video_result import StartVideoResult


pytestmark = pytest.mark.asyncio

async def test_last_media_post(client):
    """Test case for last_media_post

    Get informations about last media playback
    """
    body = {"ApiKey":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/LastMedia',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_video_post(client):
    """Test case for start_video_post

    Start the playback
    """
    body = {"ApiKey":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","MediaId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Ip":"Ip","Port":0,"AuthKey":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Collection":"Collection"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/StartVideo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

