# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_time_period200_response import GetTimePeriod200Response
from openapi_server.models.get_time_periods200_response import GetTimePeriods200Response


pytestmark = pytest.mark.asyncio

async def test_get_time_period(client):
    """Test case for get_time_period

    Get a time period
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/time_periods/{time_period_gid}'.format(time_period_gid='917392'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_time_periods(client):
    """Test case for get_time_periods

    Get time periods
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'),
                    ('start_on', '2019-09-15'),
                    ('end_on', '2019-09-15'),
                    ('workspace', '31326')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/time_periods',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

