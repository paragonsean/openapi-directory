# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_video_version_request import CreateVideoVersionRequest
from openapi_server.models.error import Error
from openapi_server.models.video_versions import VideoVersions


pytestmark = pytest.mark.asyncio

async def test_create_video_version(client):
    """Test case for create_video_version

    Add a version to a video
    """
    body = openapi_server.CreateVideoVersionRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.video.version+json',
        'Content-Type': 'application/vnd.vimeo.video.version+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/videos/{video_id}/versions'.format(video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

