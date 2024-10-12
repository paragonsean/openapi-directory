# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.energy_obs_group import EnergyObsGroup
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_history_energylatlatlonlon_get(client):
    """Test case for history_energylatlatlonlon_get

    Returns Energy API response  - Given a single lat/lon. 
    """
    params = [('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('tp', 'tp_example'),
                    ('threshold', 3.4),
                    ('units', 'units_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/energy?lat={lat}&lon={lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

