# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.video_article import VideoArticle


pytestmark = pytest.mark.asyncio

async def test_videos(client):
    """Test case for videos

    Articles with a video
    """
    params = [('page', 1),
                    ('per_page', 24)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

