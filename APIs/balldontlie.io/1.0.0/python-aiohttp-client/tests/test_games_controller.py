# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_all_games_example_parameters(client):
    """Test case for all_games_example_parameters

    all games (example parameters)
    """
    params = [('seasons[]', '2018'),
                    ('team_ids[]', '1')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/games',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specific_game(client):
    """Test case for specific_game

    specific game
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/games/32881',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

