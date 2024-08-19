# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_all_teams(client):
    """Test case for all_teams

    all teams
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/teams',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specific_team(client):
    """Test case for specific_team

    specific team
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/teams/1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

