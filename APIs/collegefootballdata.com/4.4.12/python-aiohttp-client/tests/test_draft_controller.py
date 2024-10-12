# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.draft_pick import DraftPick
from openapi_server.models.draft_position import DraftPosition
from openapi_server.models.draft_team import DraftTeam


pytestmark = pytest.mark.asyncio

async def test_get_draft_picks(client):
    """Test case for get_draft_picks

    List of NFL Draft picks
    """
    params = [('year', 56),
                    ('nflTeam', 'nfl_team_example'),
                    ('college', 'college_example'),
                    ('conference', 'conference_example'),
                    ('position', 'position_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/draft/picks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nfl_positions(client):
    """Test case for get_nfl_positions

    List of NFL positions
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/draft/positions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_nfl_teams(client):
    """Test case for get_nfl_teams

    List of NFL teams
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/draft/teams',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

