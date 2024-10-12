# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conference_sp_rating import ConferenceSPRating
from openapi_server.models.team_elo_rating import TeamEloRating
from openapi_server.models.team_sp_rating import TeamSPRating
from openapi_server.models.team_srs_rating import TeamSRSRating


pytestmark = pytest.mark.asyncio

async def test_get_conference_sp_ratings(client):
    """Test case for get_conference_sp_ratings

    Historical SP+ ratings by conference
    """
    params = [('year', 56),
                    ('conference', 'conference_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ratings/sp/conferences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_elo_ratings(client):
    """Test case for get_elo_ratings

    Historical Elo ratings
    """
    params = [('year', 56),
                    ('week', 56),
                    ('team', 'team_example'),
                    ('conference', 'conference_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ratings/elo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sp_ratings(client):
    """Test case for get_sp_ratings

    Historical SP+ ratings
    """
    params = [('year', 56),
                    ('team', 'team_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ratings/sp',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_srs_ratings(client):
    """Test case for get_srs_ratings

    Historical SRS ratings
    """
    params = [('year', 56),
                    ('team', 'team_example'),
                    ('conference', 'conference_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ratings/srs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

