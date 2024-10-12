# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.player import Player
from openapi_server.models.player_game_projection import PlayerGameProjection


pytestmark = pytest.mark.asyncio

async def test_dfs_slates_by_date(client):
    """Test case for dfs_slates_by_date

    Dfs Slates By Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/soccer/projections/{format}/DfsSlatesByDate/{_date}'.format(format='format_example', _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_injured_players_by_competition(client):
    """Test case for injured_players_by_competition

    Injured Players By Competition
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/soccer/projections/{format}/InjuredPlayers/{competition}'.format(format=xml, competition='competition_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_competition_w_dfs_salaries(client):
    """Test case for projected_player_game_stats_by_competition_w_dfs_salaries

    Projected Player Game Stats by Competition (w/ DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/soccer/projections/{format}/PlayerGameProjectionStatsByCompetition/{competition}/{_date}'.format(format=xml, competition='competition_example', _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_date_w_dfs_salaries(client):
    """Test case for projected_player_game_stats_by_date_w_dfs_salaries

    Projected Player Game Stats by Date (w/ DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/soccer/projections/{format}/PlayerGameProjectionStatsByDate/{_date}'.format(format=xml, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_player_w_dfs_salaries(client):
    """Test case for projected_player_game_stats_by_player_w_dfs_salaries

    Projected Player Game Stats by Player (w/ DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/soccer/projections/{format}/PlayerGameProjectionStatsByPlayer/{_date}/{playerid}'.format(format=xml, _date='_date_example', playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upcoming_dfs_slates_by_competition(client):
    """Test case for upcoming_dfs_slates_by_competition

    Upcoming Dfs Slates By Competition
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/soccer/projections/{format}/UpcomingDfsSlatesByCompetition/{competition_id}'.format(format='format_example', competition_id='competition_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

