# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.box_score import BoxScore
from openapi_server.models.game import Game
from openapi_server.models.game_media import GameMedia
from openapi_server.models.game_weather import GameWeather
from openapi_server.models.player_game import PlayerGame
from openapi_server.models.scoreboard_game import ScoreboardGame
from openapi_server.models.team_game import TeamGame
from openapi_server.models.team_record import TeamRecord
from openapi_server.models.week import Week


pytestmark = pytest.mark.asyncio

async def test_get_advanced_box_score(client):
    """Test case for get_advanced_box_score

    Advanced box scores
    """
    params = [('gameId', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/game/box/advanced',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_calendar(client):
    """Test case for get_calendar

    Season calendar
    """
    params = [('year', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendar',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_game_media(client):
    """Test case for get_game_media

    Game media information and schedules
    """
    params = [('year', 56),
                    ('week', 56),
                    ('seasonType', 'season_type_example'),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('mediaType', 'media_type_example'),
                    ('classification', 'classification_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/games/media',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_game_weather(client):
    """Test case for get_game_weather

    Game weather information (Patreon only)
    """
    params = [('gameId', 56),
                    ('year', 56),
                    ('week', 56),
                    ('seasonType', 'season_type_example'),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('classification', 'classification_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/games/weather',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_games(client):
    """Test case for get_games

    Games and results
    """
    params = [('year', 56),
                    ('week', 56),
                    ('seasonType', 'regular'),
                    ('team', 'team_example'),
                    ('home', 'home_example'),
                    ('away', 'away_example'),
                    ('conference', 'conference_example'),
                    ('division', 'division_example'),
                    ('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/games',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_player_game_stats(client):
    """Test case for get_player_game_stats

    Player game stats
    """
    params = [('year', 56),
                    ('week', 56),
                    ('seasonType', 'regular'),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('category', 'category_example'),
                    ('gameId', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/games/players',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scoreboard(client):
    """Test case for get_scoreboard

    Live game results (Patreon only)
    """
    params = [('classification', 'classification_example'),
                    ('conference', 'conference_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/scoreboard',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_game_stats(client):
    """Test case for get_team_game_stats

    Team game stats
    """
    params = [('year', 56),
                    ('week', 56),
                    ('seasonType', 'regular'),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('gameId', 56),
                    ('classification', 'classification_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/games/teams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_records(client):
    """Test case for get_team_records

    Team records
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
        path='/records',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

