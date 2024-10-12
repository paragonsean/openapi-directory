# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.podcast_episode_index import PodcastEpisodeIndex


pytestmark = pytest.mark.asyncio

async def test_get_podcast_episodes(client):
    """Test case for get_podcast_episodes

    Podcast Episodes
    """
    params = [('page', 1),
                    ('per_page', 30),
                    ('username', 'codenewbie')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/podcast_episodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

