# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.game_lines import GameLines


pytestmark = pytest.mark.asyncio

async def test_get_lines(client):
    """Test case for get_lines

    Betting lines
    """
    params = [('gameId', 56),
                    ('year', 56),
                    ('week', 56),
                    ('seasonType', 'regular'),
                    ('team', 'team_example'),
                    ('home', 'home_example'),
                    ('away', 'away_example'),
                    ('conference', 'conference_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/lines',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

