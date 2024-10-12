# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media import Media


pytestmark = pytest.mark.asyncio

async def test_media_post(client):
    """Test case for media_post

    Submit a new media file
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/media',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

