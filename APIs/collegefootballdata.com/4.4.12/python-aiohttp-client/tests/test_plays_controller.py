# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.live_play_by_play import LivePlayByPlay
from openapi_server.models.play import Play
from openapi_server.models.play_stat import PlayStat
from openapi_server.models.play_stat_type import PlayStatType
from openapi_server.models.play_type import PlayType


pytestmark = pytest.mark.asyncio

async def test_get_live_plays(client):
    """Test case for get_live_plays

    Live metrics and PBP (Patreon only)
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/live/plays',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_play_stat_types(client):
    """Test case for get_play_stat_types

    Types of player play stats
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/play/stat/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_play_stats(client):
    """Test case for get_play_stats

    Play stats by play
    """
    params = [('year', 56),
                    ('week', 56),
                    ('team', 'team_example'),
                    ('gameId', 56),
                    ('athleteId', 56),
                    ('statTypeId', 56),
                    ('seasonType', 'season_type_example'),
                    ('conference', 'conference_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/play/stats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_play_types(client):
    """Test case for get_play_types

    Play types
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/play/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plays(client):
    """Test case for get_plays

    Play by play data
    """
    params = [('seasonType', 'regular'),
                    ('year', 56),
                    ('week', 56),
                    ('team', 'team_example'),
                    ('offense', 'offense_example'),
                    ('defense', 'defense_example'),
                    ('conference', 'conference_example'),
                    ('offenseConference', 'offense_conference_example'),
                    ('defenseConference', 'defense_conference_example'),
                    ('playType', 56),
                    ('classification', 'classification_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/plays',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

