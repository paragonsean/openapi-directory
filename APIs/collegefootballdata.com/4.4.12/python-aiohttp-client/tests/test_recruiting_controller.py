# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.position_group_recruiting_rating import PositionGroupRecruitingRating
from openapi_server.models.recruit import Recruit
from openapi_server.models.team_recruiting_rank import TeamRecruitingRank


pytestmark = pytest.mark.asyncio

async def test_get_recruiting_groups(client):
    """Test case for get_recruiting_groups

    Recruit position group ratings
    """
    params = [('startYear', 56),
                    ('endYear', 56),
                    ('team', 'team_example'),
                    ('conference', 'conference_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recruiting/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recruiting_players(client):
    """Test case for get_recruiting_players

    Player recruiting ratings and rankings
    """
    params = [('year', 56),
                    ('classification', 'HighSchool'),
                    ('position', 'position_example'),
                    ('state', 'state_example'),
                    ('team', 'team_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recruiting/players',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recruiting_teams(client):
    """Test case for get_recruiting_teams

    Team recruiting rankings and ratings
    """
    params = [('year', 56),
                    ('team', 'team_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recruiting/teams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

