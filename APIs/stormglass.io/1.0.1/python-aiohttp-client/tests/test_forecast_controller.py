# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.forecast import Forecast


pytestmark = pytest.mark.asyncio

async def test_get_forecast(client):
    """Test case for get_forecast

    Get hourly forecasts by coordinates
    """
    params = [('lat', 3.4),
                    ('lng', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'authenticationToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/forecast',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

