# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.play_by_play import PlayByPlay


pytestmark = pytest.mark.asyncio

async def test_play_by_play(client):
    """Test case for play_by_play

    Play By Play
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/pbp/{format}/PlayByPlay/{gameid}'.format(format=XML, gameid='gameid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_play_by_play_delta(client):
    """Test case for play_by_play_delta

    Play By Play Delta
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/mlb/pbp/{format}/PlayByPlayDelta/{_date}/{minutes}'.format(format=XML, _date='_date_example', minutes='minutes_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

