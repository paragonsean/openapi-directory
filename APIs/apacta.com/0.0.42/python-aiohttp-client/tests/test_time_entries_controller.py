# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.time_entries_get200_response import TimeEntriesGet200Response
from openapi_server.models.time_entries_post_request import TimeEntriesPostRequest
from openapi_server.models.time_entries_time_entry_id_get200_response import TimeEntriesTimeEntryIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_time_entries_get(client):
    """Test case for time_entries_get

    List time entries
    """
    params = [('user_id', 'user_id_example'),
                    ('form_id', 'form_id_example'),
                    ('project_id', 'project_id_example'),
                    ('gt_from_time', 'gt_from_time_example'),
                    ('lt_from_time', 'lt_from_time_example'),
                    ('gt_to_time', 'gt_to_time_example'),
                    ('lt_to_time', 'lt_to_time_example'),
                    ('lt_sum', 'lt_sum_example'),
                    ('gt_sum', 'gt_sum_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/time_entries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entries_post(client):
    """Test case for time_entries_post

    Add new time entry
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
        path='/api/v1/time_entries',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entries_time_entry_id_delete(client):
    """Test case for time_entries_time_entry_id_delete

    Delete time entry
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/time_entries/{time_entry_id}'.format(time_entry_id='time_entry_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entries_time_entry_id_get(client):
    """Test case for time_entries_time_entry_id_get

    View time entry
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/time_entries/{time_entry_id}'.format(time_entry_id='time_entry_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entries_time_entry_id_put(client):
    """Test case for time_entries_time_entry_id_put

    Edit time entry
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/time_entries/{time_entry_id}'.format(time_entry_id='time_entry_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

