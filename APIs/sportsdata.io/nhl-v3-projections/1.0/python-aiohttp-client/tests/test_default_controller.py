# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
from openapi_server.models.player import Player
from openapi_server.models.player_game_projection import PlayerGameProjection
from openapi_server.models.starting_goaltenders import StartingGoaltenders


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
        path='/v3/nhl/projections/{format}/DfsSlatesByDate/{_date}'.format(format=XML, _date='_date_example'),
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
        path='/v3/nhl/projections/{format}/InjuredPlayers'.format(format=XML),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_date_w_injuries_dfs_salaries(client):
    """Test case for projected_player_game_stats_by_date_w_injuries_dfs_salaries

    Projected Player Game Stats by Date (w/ Injuries, DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nhl/projections/{format}/PlayerGameProjectionStatsByDate/{_date}'.format(format=XML, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_player_w_injuries_dfs_salaries(client):
    """Test case for projected_player_game_stats_by_player_w_injuries_dfs_salaries

    Projected Player Game Stats by Player (w/ Injuries, DFS Salaries)
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nhl/projections/{format}/PlayerGameProjectionStatsByPlayer/{_date}/{playerid}'.format(format=XML, _date='_date_example', playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_starting_goaltenders_by_date(client):
    """Test case for starting_goaltenders_by_date

    Starting Goaltenders by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/nhl/projections/{format}/StartingGoaltendersByDate/{_date}'.format(format=XML, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

