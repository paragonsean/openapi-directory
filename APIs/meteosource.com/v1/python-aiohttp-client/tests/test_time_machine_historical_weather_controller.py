# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.general_request_error import GeneralRequestError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.time_machine_time_machine import TimeMachineTimeMachine
from openapi_server.models.units import Units


pytestmark = pytest.mark.asyncio

async def test_time_machine_time_machine_get(client):
    """Test case for time_machine_time_machine_get

    Returns weather data for a single location and given day in the past
    """
    params = [('place_id', 'place_id_example'),
                    ('lat', 'lat_example'),
                    ('lon', 'lon_example'),
                    ('date', '2013-10-20'),
                    ('timezone', 'timezone_example'),
                    ('units', openapi_server.Units()),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'APIKeyHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/premium/time_machine',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

