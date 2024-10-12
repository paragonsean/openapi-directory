# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.time_entries_post_request import TimeEntriesPostRequest
from openapi_server.models.time_entry_rates_get200_response import TimeEntryRatesGet200Response
from openapi_server.models.time_entry_rates_time_entry_rate_id_get200_response import TimeEntryRatesTimeEntryRateIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_time_entry_rates_get(client):
    """Test case for time_entry_rates_get

    List time entry rates
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/time_entry_rates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_rates_post(client):
    """Test case for time_entry_rates_post

    Add new time entry rate
    """
    body = openapi_server.TimeEntriesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/time_entry_rates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_rates_time_entry_rate_id_get(client):
    """Test case for time_entry_rates_time_entry_rate_id_get

    View time entry rate
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/time_entry_rates/{time_entry_rate_id}'.format(time_entry_rate_id='time_entry_rate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_rates_time_entry_rate_id_put(client):
    """Test case for time_entry_rates_time_entry_rate_id_put

    Edit time entry rate
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/time_entry_rates/{time_entry_rate_id}'.format(time_entry_rate_id='time_entry_rate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

