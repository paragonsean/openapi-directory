# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.game import Game
from openapi_server.models.news import News
from openapi_server.models.player import Player
from openapi_server.models.player_basic import PlayerBasic
from openapi_server.models.schedule_basic import ScheduleBasic
from openapi_server.models.score_basic import ScoreBasic
from openapi_server.models.season import Season
from openapi_server.models.stadium import Stadium
from openapi_server.models.standing import Standing
from openapi_server.models.team import Team
from openapi_server.models.team_game import TeamGame
from openapi_server.models.team_season import TeamSeason


pytestmark = pytest.mark.asyncio

async def test_are_games_in_progress(client):
    """Test case for are_games_in_progress

    Are Games In Progress
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/AreAnyGamesInProgress'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_current_season(client):
    """Test case for current_season

    Current Season
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/CurrentSeason'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_by_date(client):
    """Test case for games_by_date

    Games by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/GamesByDate/{_date}'.format(format=XML, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_games_by_date_basic(client):
    """Test case for games_by_date_basic

    Games by Date (Basic)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/ScoresBasic/{_date}'.format(format=XML, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_news(client):
    """Test case for news

    News
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/News'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_news_by_date(client):
    """Test case for news_by_date

    News by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/NewsByDate/{_date}'.format(format=XML, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_news_by_player(client):
    """Test case for news_by_player

    News by Player
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/NewsByPlayerID/{playerid}'.format(format=XML, playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_details_by_active(client):
    """Test case for player_details_by_active

    Player Details by Active
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/Players'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_details_by_free_agents(client):
    """Test case for player_details_by_free_agents

    Player Details by Free Agents
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/FreeAgents'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_details_by_player(client):
    """Test case for player_details_by_player

    Player Details by Player
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/Player/{playerid}'.format(format=XML, playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_players_by_team(client):
    """Test case for players_by_team

    Players by Team
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/Players/{team}'.format(format=XML, team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_players_by_team_basic(client):
    """Test case for players_by_team_basic

    Players by Team (Basic)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/PlayersBasic/{team}'.format(format=XML, team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules(client):
    """Test case for schedules

    Schedules
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/Games/{season}'.format(format=XML, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedules_basic(client):
    """Test case for schedules_basic

    Schedules (Basic)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/SchedulesBasic/{season}'.format(format=XML, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stadiums(client):
    """Test case for stadiums

    Stadiums
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/Stadiums'.format(format=xml),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_standings(client):
    """Test case for standings

    Standings
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/Standings/{season}'.format(format=XML, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_game_logs_by_season(client):
    """Test case for team_game_logs_by_season

    Team Game Logs By Season
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}'.format(format=XML, season='season_example', teamid='teamid_example', numberofgames='numberofgames_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_game_stats_by_date(client):
    """Test case for team_game_stats_by_date

    Team Game Stats by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/TeamGameStatsByDate/{_date}'.format(format=XML, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_season_stats(client):
    """Test case for team_season_stats

    Team Season Stats
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/TeamSeasonStats/{season}'.format(format=XML, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_active(client):
    """Test case for teams_active

    Teams (Active)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/teams'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_all(client):
    """Test case for teams_all

    Teams (All)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/scores/{format}/AllTeams'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

