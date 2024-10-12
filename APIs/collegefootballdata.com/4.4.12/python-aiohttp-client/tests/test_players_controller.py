# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.player_search_result import PlayerSearchResult
from openapi_server.models.player_season_stat import PlayerSeasonStat
from openapi_server.models.player_usage import PlayerUsage
from openapi_server.models.portal_player import PortalPlayer
from openapi_server.models.returning_production import ReturningProduction


pytestmark = pytest.mark.asyncio

async def test_get_player_season_stats(client):
    """Test case for get_player_season_stats

    Player stats by season
    """
    params = [('year', 56),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('startWeek', 56),
                    ('endWeek', 56),
                    ('seasonType', 'season_type_example'),
                    ('category', 'category_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/stats/player/season',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_player_usage(client):
    """Test case for get_player_usage

    Player usage metrics broken down by season
    """
    params = [('year', 2022),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('position', 'position_example'),
                    ('playerId', 56),
                    ('excludeGarbageTime', True)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/player/usage',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_returning_production(client):
    """Test case for get_returning_production

    Team returning production metrics
    """
    params = [('year', 56),
                    ('team', 'team_example'),
                    ('conference', 'conference_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/player/returning',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transfer_portal(client):
    """Test case for get_transfer_portal

    Transfer portal by season
    """
    params = [('year', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/player/portal',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_search(client):
    """Test case for player_search

    Search for player information
    """
    params = [('searchTerm', 'search_term_example'),
                    ('position', 'position_example'),
                    ('team', 'team_example'),
                    ('year', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/player/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

