# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_all_stats_example_parameters(client):
    """Test case for all_stats_example_parameters

    all stats (example parameters)
    """
    params = [('season[]', '2018'),
                    ('player_ids[]', '237')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/stats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

