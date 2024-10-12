# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.news import News


pytestmark = pytest.mark.asyncio

async def test_premium_news(client):
    """Test case for premium_news

    Premium News
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/news-rotoballer/{format}/RotoBallerPremiumNews'.format(format=xml),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_premium_news_by_date(client):
    """Test case for premium_news_by_date

    Premium News by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/news-rotoballer/{format}/RotoBallerPremiumNewsByDate/{_date}'.format(format=xml, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_premium_news_by_player(client):
    """Test case for premium_news_by_player

    Premium News by Player
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/news-rotoballer/{format}/RotoBallerPremiumNewsByPlayerID/{playerid}'.format(format=xml, playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

