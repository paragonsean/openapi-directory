# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.energy_obs_group_forecast import EnergyObsGroupForecast
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_forecast_energylatlatlonlon_get(client):
    """Test case for forecast_energylatlatlonlon_get

    Returns Energy Forecast API response  - Given a single lat/lon. 
    """
    params = [('threshold', 3.4),
                    ('units', 'units_example'),
                    ('tp', 'tp_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/energy?lat={lat}&lon={lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

