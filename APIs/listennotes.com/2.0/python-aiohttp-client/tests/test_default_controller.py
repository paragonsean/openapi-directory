# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.podcast_minimum_rss import PodcastMinimumRss
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE


pytestmark = pytest.mark.asyncio

async def test_podcast_deleted_post(client):
    """Test case for podcast_deleted_post

    
    """
    podcast_minimum_rss = openapi_server.PodcastMinimumRss()
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/v2/podcastDeleted',
        headers=headers,
        json=podcast_minimum_rss,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_podcasts_submit_accepted_post(client):
    """Test case for podcasts_submit_accepted_post

    
    """
    podcast_minimum_rss = openapi_server.PodcastMinimumRss()
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/v2/podcastsSubmitAccepted',
        headers=headers,
        json=podcast_minimum_rss,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_podcasts_submit_rejected_post(client):
    """Test case for podcasts_submit_rejected_post

    
    """
    unknown_base_type = openapi_server.UNKNOWN_BASE_TYPE()
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/v2/podcastsSubmitRejected',
        headers=headers,
        json=unknown_base_type,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

