# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.dfs_slate_with_ownership_projection import DfsSlateWithOwnershipProjection
from openapi_server.models.fantasy_defense_game_projection import FantasyDefenseGameProjection
from openapi_server.models.fantasy_defense_season_projection import FantasyDefenseSeasonProjection
from openapi_server.models.player import Player
from openapi_server.models.player_game_projection import PlayerGameProjection
from openapi_server.models.player_season_projection import PlayerSeasonProjection


pytestmark = pytest.mark.asyncio

async def test_dfs_slate_ownership_projections_by_slateid(client):
    """Test case for dfs_slate_ownership_projections_by_slateid

    DFS Slate Ownership Projections by SlateID
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/DfsSlateOwnershipProjectionsBySlateID/{slate_id}'.format(format=XML, slate_id='slate_id_example'),
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
        path='/v3/nfl/projections/{format}/DfsSlatesByDate/{_date}'.format(format=XML, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dfs_slates_by_week(client):
    """Test case for dfs_slates_by_week

    DFS Slates by Week
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/DfsSlatesByWeek/{season}/{week}'.format(format=XML, season='season_example', week='week_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_idp_projected_player_game_stats_by_player_w_injuries_lineups_dfs_salaries(client):
    """Test case for idp_projected_player_game_stats_by_player_w_injuries_lineups_dfs_salaries

    IDP Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/IdpPlayerGameProjectionStatsByPlayerID/{season}/{week}/{playerid}'.format(format=XML, season='season_example', week='week_example', playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_idp_projected_player_game_stats_by_team_w_injuries_lineups_dfs_salaries(client):
    """Test case for idp_projected_player_game_stats_by_team_w_injuries_lineups_dfs_salaries

    IDP Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/IdpPlayerGameProjectionStatsByTeam/{season}/{week}/{team}'.format(format=XML, season='season_example', week='week_example', team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_idp_projected_player_game_stats_by_week_w_injuries_lineups_dfs_salaries(client):
    """Test case for idp_projected_player_game_stats_by_week_w_injuries_lineups_dfs_salaries

    IDP Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/IdpPlayerGameProjectionStatsByWeek/{season}/{week}'.format(format=XML, season='season_example', week='week_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_injured_players(client):
    """Test case for injured_players

    Injured Players
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/InjuredPlayers'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_fantasy_defense_game_stats_w_dfs_salaries(client):
    """Test case for projected_fantasy_defense_game_stats_w_dfs_salaries

    Projected Fantasy Defense Game Stats (w/ DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/FantasyDefenseProjectionsByGame/{season}/{week}'.format(format=XML, season='season_example', week='week_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_fantasy_defense_season_stats_w_adp(client):
    """Test case for projected_fantasy_defense_season_stats_w_adp

    Projected Fantasy Defense Season Stats (w/ ADP)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/FantasyDefenseProjectionsBySeason/{season}'.format(format=XML, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_player_w_injuries_lineups_dfs_salaries(client):
    """Test case for projected_player_game_stats_by_player_w_injuries_lineups_dfs_salaries

    Projected Player Game Stats by Player (w/ Injuries, Lineups, DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/PlayerGameProjectionStatsByPlayerID/{season}/{week}/{playerid}'.format(format=XML, season='season_example', week='week_example', playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_team_w_injuries_lineups_dfs_salaries(client):
    """Test case for projected_player_game_stats_by_team_w_injuries_lineups_dfs_salaries

    Projected Player Game Stats by Team (w/ Injuries, Lineups, DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/PlayerGameProjectionStatsByTeam/{season}/{week}/{team}'.format(format=XML, season='season_example', week='week_example', team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_week_w_injuries_lineups_dfs_salaries(client):
    """Test case for projected_player_game_stats_by_week_w_injuries_lineups_dfs_salaries

    Projected Player Game Stats by Week (w/ Injuries, Lineups, DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/PlayerGameProjectionStatsByWeek/{season}/{week}'.format(format=XML, season='season_example', week='week_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_season_stats_by_player_w_adp(client):
    """Test case for projected_player_season_stats_by_player_w_adp

    Projected Player Season Stats by Player (w/ ADP)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/PlayerSeasonProjectionStatsByPlayerID/{season}/{playerid}'.format(format=XML, season='season_example', playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_season_stats_by_team_w_adp(client):
    """Test case for projected_player_season_stats_by_team_w_adp

    Projected Player Season Stats by Team (w/ ADP)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/PlayerSeasonProjectionStatsByTeam/{season}/{team}'.format(format=XML, season='season_example', team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_season_stats_w_adp(client):
    """Test case for projected_player_season_stats_w_adp

    Projected Player Season Stats (w/ ADP)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/PlayerSeasonProjectionStats/{season}'.format(format=XML, season='season_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upcoming_dfs_slate_ownership_projections(client):
    """Test case for upcoming_dfs_slate_ownership_projections

    Upcoming DFS Slate Ownership Projections
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nfl/projections/{format}/UpcomingDfsSlateOwnershipProjections'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

