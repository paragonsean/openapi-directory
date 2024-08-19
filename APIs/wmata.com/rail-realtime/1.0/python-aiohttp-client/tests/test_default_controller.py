# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_call547636a6f918230da855363f(client):
    """Test case for call547636a6f918230da855363f

    JSON - Next Trains
    """
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/StationPrediction.svc/json/GetPrediction/{station_codes}'.format(station_codes=B03),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call547636a6f918230da8553640(client):
    """Test case for call547636a6f918230da8553640

    XML - Next Trains
    """
    headers = { 
        'Accept': 'text/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/StationPrediction.svc/GetPrediction/{station_codes}'.format(station_codes=B03),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

