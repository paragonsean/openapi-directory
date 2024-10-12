# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.podcast_episode_list import PodcastEpisodeList
from openapi_server.models.podcast_list import PodcastList
from openapi_server.models.single_podcast import SinglePodcast


pytestmark = pytest.mark.asyncio

async def test_podcasts_get(client):
    """Test case for podcasts_get

    
    """
    params = [('page', 'page_example'),
                    ('pageSize', 'page_size_example'),
                    ('order', 'order_example'),
                    ('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'partner_id': 'special-key',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/partner/podcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_podcasts_podcast_id_episodes_get(client):
    """Test case for podcasts_podcast_id_episodes_get

    
    """
    params = [('page', 'page_example'),
                    ('pageSize', 'page_size_example'),
                    ('order', 'order_example'),
                    ('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'partner_id': 'special-key',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/partner/podcasts/{podcast_id}/episodes'.format(podcast_id='podcast_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_podcasts_podcast_id_get(client):
    """Test case for podcasts_podcast_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'partner_id': 'special-key',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/partner/podcasts/{podcast_id}'.format(podcast_id='podcast_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

