# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.weather_alert import WeatherAlert


pytestmark = pytest.mark.asyncio

async def test_alertslatlatlonlon_get(client):
    """Test case for alertslatlatlonlon_get

    Returns severe weather alerts issued by meteorological agencies - Given a lat/lon.
    """
    params = [('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/alerts?lat={lat}&lon={lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

