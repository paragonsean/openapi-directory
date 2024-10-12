# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advanced_game_stat import AdvancedGameStat
from openapi_server.models.advanced_season_stat import AdvancedSeasonStat
from openapi_server.models.team_season_stat import TeamSeasonStat


pytestmark = pytest.mark.asyncio

async def test_get_advanced_team_game_stats(client):
    """Test case for get_advanced_team_game_stats

    Advanced team metrics by game
    """
    params = [('year', 56),
                    ('week', 56),
                    ('team', 'team_example'),
                    ('opponent', 'opponent_example'),
                    ('excludeGarbageTime', True),
                    ('seasonType', 'season_type_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/game/advanced',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_advanced_team_season_stats(client):
    """Test case for get_advanced_team_season_stats

    Advanced team metrics by season
    """
    params = [('year', 56),
                    ('team', 'team_example'),
                    ('excludeGarbageTime', True),
                    ('startWeek', 56),
                    ('endWeek', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/season/advanced',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stat_categories(client):
    """Test case for get_stat_categories

    Team stat categories
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_season_stats(client):
    """Test case for get_team_season_stats

    Team statistics by season
    """
    params = [('year', 56),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('startWeek', 56),
                    ('endWeek', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/season',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

