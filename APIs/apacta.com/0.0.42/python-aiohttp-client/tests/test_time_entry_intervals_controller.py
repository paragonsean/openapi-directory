# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.time_entry_intervals_get200_response import TimeEntryIntervalsGet200Response
from openapi_server.models.time_entry_intervals_time_entry_interval_id_get200_response import TimeEntryIntervalsTimeEntryIntervalIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_time_entry_intervals_get(client):
    """Test case for time_entry_intervals_get

    List possible time entry intervals
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/time_entry_intervals',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_intervals_time_entry_interval_id_get(client):
    """Test case for time_entry_intervals_time_entry_interval_id_get

    View time entry interval
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/time_entry_intervals/{time_entry_interval_id}'.format(time_entry_interval_id='time_entry_interval_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

