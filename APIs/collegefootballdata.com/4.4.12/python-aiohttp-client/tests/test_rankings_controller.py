# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ranking_week import RankingWeek


pytestmark = pytest.mark.asyncio

async def test_get_rankings(client):
    """Test case for get_rankings

    Historical polls and rankings
    """
    params = [('year', 56),
                    ('week', 56),
                    ('seasonType', 'regular')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rankings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

