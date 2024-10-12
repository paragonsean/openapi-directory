# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.article import Article


pytestmark = pytest.mark.asyncio

async def test_rotoballer_articles(client):
    """Test case for rotoballer_articles

    RotoBaller Articles
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/articles-rotoballer/{format}/RotoBallerArticles'.format(format=xml),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rotoballer_articles_by_date(client):
    """Test case for rotoballer_articles_by_date

    RotoBaller Articles by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/articles-rotoballer/{format}/RotoBallerArticlesByDate/{_date}'.format(format=xml, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rotoballer_articles_by_player(client):
    """Test case for rotoballer_articles_by_player

    RotoBaller Articles by Player
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/articles-rotoballer/{format}/RotoBallerArticlesByPlayerID/{playerid}'.format(format=xml, playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

