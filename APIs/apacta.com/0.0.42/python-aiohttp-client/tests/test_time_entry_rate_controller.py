# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response


pytestmark = pytest.mark.asyncio

async def test_time_entry_rates_time_entry_rate_id_delete(client):
    """Test case for time_entry_rates_time_entry_rate_id_delete

    Delete time entry rate
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/time_entry_rates/{time_entry_rate_id}'.format(time_entry_rate_id='time_entry_rate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

