# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_news_feed_card_analytics_0(client):
    """Test case for news_feed_card_analytics_0

    News Feed Card Analytics
    """
    params = [('card_id', '{{card_identifier}}'),
                    ('length', '14'),
                    ('unit', 'day'),
                    ('ending_at', '2018-06-28T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/feed/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_news_feed_cards_details_0(client):
    """Test case for news_feed_cards_details_0

    News Feed Cards Details
    """
    params = [('card_id', '{{card_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/feed/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_news_feed_cards_list_0(client):
    """Test case for news_feed_cards_list_0

    News Feed Cards List
    """
    params = [('page', '1'),
                    ('include_archived', 'true'),
                    ('sort_direction', 'desc')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/feed/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

