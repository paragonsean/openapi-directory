# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.box_score import BoxScore
from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.game import Game
from openapi_server.models.news import News
from openapi_server.models.player import Player
from openapi_server.models.player_game import PlayerGame
from openapi_server.models.player_info import PlayerInfo
from openapi_server.models.player_season import PlayerSeason
from openapi_server.models.season import Season
from openapi_server.models.stadium import Stadium
from openapi_server.models.standing import Standing
from openapi_server.models.team import Team
from openapi_server.models.team_game import TeamGame
from openapi_server.models.team_season import TeamSeason


pytestmark = pytest.mark.asyncio

async def test_all_stars(client):
    """Test case for all_stars

    All-Stars
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/AllStars/{season}'.format(format=XML, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


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
        path='/v3/nba/stats/{format}/AreAnyGamesInProgress'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_box_score(client):
    """Test case for box_score

    Box Score
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/BoxScore/{gameid}'.format(format=XML, gameid='gameid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_box_scores_by_date(client):
    """Test case for box_scores_by_date

    Box Scores by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/BoxScores/{_date}'.format(format=XML, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_box_scores_by_date_delta(client):
    """Test case for box_scores_by_date_delta

    Box Scores by Date Delta
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/BoxScoresDelta/{_date}/{minutes}'.format(format=XML, _date='_date_example', minutes='minutes_example'),
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
        path='/v3/nba/stats/{format}/CurrentSeason'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfs_slates_by_date(client):
    """Test case for dfs_slates_by_date

    DFS Slates by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/DfsSlatesByDate/{_date}'.format(format=XML, _date='_date_example'),
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
        path='/v3/nba/stats/{format}/GamesByDate/{_date}'.format(format=XML, _date='_date_example'),
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
        path='/v3/nba/stats/{format}/News'.format(format=XML),
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
        path='/v3/nba/stats/{format}/NewsByDate/{_date}'.format(format=XML, _date='_date_example'),
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
        path='/v3/nba/stats/{format}/NewsByPlayerID/{playerid}'.format(format=XML, playerid='playerid_example'),
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
        path='/v3/nba/stats/{format}/Players'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_details_by_free_agent(client):
    """Test case for player_details_by_free_agent

    Player Details by Free Agent
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/FreeAgents'.format(format=XML),
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
        path='/v3/nba/stats/{format}/Player/{playerid}'.format(format=XML, playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_game_logs_by_season(client):
    """Test case for player_game_logs_by_season

    Player Game Logs By Season
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/PlayerGameStatsBySeason/{season}/{playerid}/{numberofgames}'.format(format=XML, season='season_example', playerid='playerid_example', numberofgames='numberofgames_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_game_stats_by_date(client):
    """Test case for player_game_stats_by_date

    Player Game Stats by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/PlayerGameStatsByDate/{_date}'.format(format=XML, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_game_stats_by_player(client):
    """Test case for player_game_stats_by_player

    Player Game Stats by Player
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/PlayerGameStatsByPlayer/{_date}/{playerid}'.format(format=XML, _date='_date_example', playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_season_stats(client):
    """Test case for player_season_stats

    Player Season Stats
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/PlayerSeasonStats/{season}'.format(format=XML, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_season_stats_by_player(client):
    """Test case for player_season_stats_by_player

    Player Season Stats By Player
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/PlayerSeasonStatsByPlayer/{season}/{playerid}'.format(format=XML, season='season_example', playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_player_season_stats_by_team(client):
    """Test case for player_season_stats_by_team

    Player Season Stats by Team
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/PlayerSeasonStatsByTeam/{season}/{team}'.format(format=XML, season='season_example', team='team_example'),
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
        path='/v3/nba/stats/{format}/Players/{team}'.format(format=XML, team='team_example'),
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
        path='/v3/nba/stats/{format}/Games/{season}'.format(format=XML, season='season_example'),
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
        path='/v3/nba/stats/{format}/Stadiums'.format(format=xml),
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
        path='/v3/nba/stats/{format}/Standings/{season}'.format(format=XML, season='season_example'),
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
        path='/v3/nba/stats/{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames}'.format(format=XML, season='season_example', teamid='teamid_example', numberofgames='numberofgames_example'),
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
        path='/v3/nba/stats/{format}/TeamGameStatsByDate/{_date}'.format(format=XML, _date='_date_example'),
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
        path='/v3/nba/stats/{format}/TeamSeasonStats/{season}'.format(format=XML, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_team_stats_allowed_by_position(client):
    """Test case for team_stats_allowed_by_position

    Team Stats Allowed by Position
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nba/stats/{format}/TeamStatsAllowedByPosition/{season}'.format(format=XML, season='season_example'),
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
        path='/v3/nba/stats/{format}/teams'.format(format=XML),
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
        path='/v3/nba/stats/{format}/AllTeams'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

