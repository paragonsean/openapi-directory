# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_api_icaro_endpoints_icaro_ambient_dose200_response import AppApiIcaroEndpointsICAROAmbientDose200Response
from openapi_server.models.app_api_icaro_endpoints_icaro_effective_dose200_response import AppApiIcaroEndpointsICAROEffectiveDose200Response


pytestmark = pytest.mark.asyncio

async def test_app_api_icaro_endpoints_icaro_ambient_dose(client):
    """Test case for app_api_icaro_endpoints_icaro_ambient_dose

    Calculate the ambient equivalent dose along a great circle flight route. 
    """
    params = [('origin', 'YSSY'),
                    ('destination', '33.94250107,-118.4079971'),
                    ('altitude', 10.1),
                    ('duration', 5),
                    ('initial_altitude', 0),
                    ('cruising_altitudes', [[10,15]]),
                    ('climb_times', [[0.1,0.5]]),
                    ('cruising_times', [[1,2]]),
                    ('descent_time', 0.5),
                    ('final_altitude', 0),
                    ('year', 2019),
                    ('month', 5),
                    ('day', 21)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/route/ambient_dose',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_api_icaro_endpoints_icaro_effective_dose(client):
    """Test case for app_api_icaro_endpoints_icaro_effective_dose

    Calculate the total effective dose along a great circle flight route. 
    """
    params = [('origin', 'YSSY'),
                    ('destination', '33.94250107,-118.4079971'),
                    ('altitude', 10.1),
                    ('duration', 5),
                    ('initial_altitude', 0),
                    ('cruising_altitudes', [[10,15]]),
                    ('climb_times', [[0.1,0.5]]),
                    ('cruising_times', [[1,2]]),
                    ('descent_time', 0.5),
                    ('final_altitude', 0),
                    ('year', 2019),
                    ('month', 5),
                    ('day', 21)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/route/effective_dose',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

