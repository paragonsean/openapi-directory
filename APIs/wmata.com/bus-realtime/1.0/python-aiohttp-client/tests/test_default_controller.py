# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_call5476365e031f5909e4fe331d(client):
    """Test case for call5476365e031f5909e4fe331d

    JSON - Next Buses
    """
    params = [('StopID', 1001195)]
    headers = { 
        'Accept': 'application/json',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NextBusService.svc/json/jPredictions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call5476365e031f5909e4fe331e(client):
    """Test case for call5476365e031f5909e4fe331e

    XML - Next Buses
    """
    params = [('StopID', 1001195)]
    headers = { 
        'Accept': 'application/xml',
        'apiKeyQuery': 'special-key',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NextBusService.svc/Predictions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

