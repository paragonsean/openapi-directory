# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dfs_slate import DfsSlate
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
        path='/v3/lol/projections/{format}/DfsSlatesByDate/{_date}'.format(format='format_example', _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_date(client):
    """Test case for projected_player_game_stats_by_date

    Projected Player Game Stats by Date
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/lol/projections/{format}/PlayerGameProjectionStatsByDate/{_date}'.format(format=xml, _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projected_player_game_stats_by_player(client):
    """Test case for projected_player_game_stats_by_player

    Projected Player Game Stats by Player
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/lol/projections/{format}/PlayerGameProjectionStatsByPlayer/{_date}/{playerid}'.format(format=xml, _date='_date_example', playerid='playerid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

