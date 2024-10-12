# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.player import Player
from openapi_server.models.team import Team
from openapi_server.models.team_matchup import TeamMatchup
from openapi_server.models.team_talent import TeamTalent


pytestmark = pytest.mark.asyncio

async def test_get_fbs_teams(client):
    """Test case for get_fbs_teams

    FBS team list
    """
    params = [('year', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/teams/fbs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_roster(client):
    """Test case for get_roster

    Team rosters
    """
    params = [('team', 'team_example'),
                    ('year', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/roster',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_talent(client):
    """Test case for get_talent

    Team talent composite rankings
    """
    params = [('year', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/talent',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_matchup(client):
    """Test case for get_team_matchup

    Team matchup history
    """
    params = [('team1', 'team1_example'),
                    ('team2', 'team2_example'),
                    ('minYear', 56),
                    ('maxYear', 56)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/teams/matchup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_teams(client):
    """Test case for get_teams

    Team information
    """
    params = [('conference', 'conference_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/teams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

