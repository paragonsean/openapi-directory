# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_all_players_search(client):
    """Test case for all_players_search

    all players (search)
    """
    params = [('search', 'lebron')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/players',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specific_player(client):
    """Test case for specific_player

    specific player
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/players/237',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

