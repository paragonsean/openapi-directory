# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_related_hashtags(client):
    """Test case for get_related_hashtags

    Gets related hashtags for a show.
    """
    params = [('showID', 'show_id_example'),
                    ('timeWindow', 'time_window_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/hashtag/related',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trending_shows(client):
    """Test case for get_trending_shows

    Gets trending shows.
    """
    params = [('limit', 'limit_example'),
                    ('timeWindow', 'time_window_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/hashtag/trendingShows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tunein_links(client):
    """Test case for get_tunein_links

    Gets tunein URLs (links) from either a tweet, hashtags, @mentions, or show ID.
    """
    params = [('tweet', 'tweet_example'),
                    ('hashtags', 'hashtags_example'),
                    ('showID', 'show_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/hashtag/tuneinlinks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

