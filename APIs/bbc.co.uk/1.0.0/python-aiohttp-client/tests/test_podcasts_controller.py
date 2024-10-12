# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.podcast_episodes_response import PodcastEpisodesResponse
from openapi_server.models.podcast_error_response import PodcastErrorResponse
from openapi_server.models.podcasts_featured_response import PodcastsFeaturedResponse
from openapi_server.models.podcasts_response import PodcastsResponse


pytestmark = pytest.mark.asyncio

async def test_get_podcast_by_pid(client):
    """Test case for get_podcast_by_pid

    Podcast
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/podcasts/{pid}'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcast_episodes(client):
    """Test case for get_podcast_episodes

    Podcast Episodes
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/podcasts/{pid}/episodes'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcasts(client):
    """Test case for get_podcasts

    All Podcasts
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('sort', 'sort_example'),
                    ('network', 'network_example'),
                    ('network_url_key', 'network_url_key_example'),
                    ('category', 'category_example'),
                    ('q', 'q_example'),
                    ('coverage', 'coverage_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/podcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcasts_featured(client):
    """Test case for get_podcasts_featured

    Featured Podcasts
    """
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/podcasts/featured',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

