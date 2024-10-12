# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.position import Position


pytestmark = pytest.mark.asyncio

async def test_positions_get(client):
    """Test case for positions_get

    Fetches a list of Positions
    """
    params = [('deviceId', 56),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/positions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

