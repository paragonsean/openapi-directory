# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.statistics import Statistics


pytestmark = pytest.mark.asyncio

async def test_statistics_get(client):
    """Test case for statistics_get

    Fetch server Statistics
    """
    params = [('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/statistics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

