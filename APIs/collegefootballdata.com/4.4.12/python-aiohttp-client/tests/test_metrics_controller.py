# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.game_ppa import GamePPA
from openapi_server.models.play_wp import PlayWP
from openapi_server.models.player_game_ppa import PlayerGamePPA
from openapi_server.models.player_season_ppa import PlayerSeasonPPA
from openapi_server.models.predicted_points import PredictedPoints
from openapi_server.models.pregame_wp import PregameWP
from openapi_server.models.team_ppa import TeamPPA


pytestmark = pytest.mark.asyncio

async def test_get_game_ppa(client):
    """Test case for get_game_ppa

    Team Predicated Points Added (PPA/EPA) by game
    """
    params = [('year', 56),
                    ('week', 56),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('excludeGarbageTime', True),
                    ('seasonType', 'regular')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ppa/games',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_player_game_ppa(client):
    """Test case for get_player_game_ppa

    Player Predicated Points Added (PPA/EPA) broken down by game
    """
    params = [('year', 56),
                    ('week', 56),
                    ('team', 'team_example'),
                    ('position', 'position_example'),
                    ('playerId', 56),
                    ('threshold', 'threshold_example'),
                    ('excludeGarbageTime', True),
                    ('seasonType', 'regular')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ppa/players/games',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_player_season_ppa(client):
    """Test case for get_player_season_ppa

    Player Predicated Points Added (PPA/EPA) broken down by season
    """
    params = [('year', 56),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('position', 'position_example'),
                    ('playerId', 56),
                    ('threshold', 'threshold_example'),
                    ('excludeGarbageTime', True)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ppa/players/season',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_predicted_points(client):
    """Test case for get_predicted_points

    Predicted Points (i.e. Expected Points or EP)
    """
    params = [('down', 56),
                    ('distance', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ppa/predicted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pregame_win_probabilities(client):
    """Test case for get_pregame_win_probabilities

    Pregame win probability data
    """
    params = [('year', 56),
                    ('week', 56),
                    ('team', 'team_example'),
                    ('seasonType', 'season_type_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metrics/wp/pregame',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_ppa(client):
    """Test case for get_team_ppa

    Predicted Points Added (PPA/EPA) data by team
    """
    params = [('year', 56),
                    ('team', 'team_example'),
                    ('conference', 'conference_example'),
                    ('excludeGarbageTime', True)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ppa/teams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_win_probability_data(client):
    """Test case for get_win_probability_data

    Win probability chart data
    """
    params = [('gameId', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/metrics/wp',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

