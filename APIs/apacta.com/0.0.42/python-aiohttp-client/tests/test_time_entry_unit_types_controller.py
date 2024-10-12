# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.time_entry_unit_types_get200_response import TimeEntryUnitTypesGet200Response
from openapi_server.models.time_entry_unit_types_time_entry_unit_type_id_get200_response import TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_time_entry_unit_types_get(client):
    """Test case for time_entry_unit_types_get

    List possible time entry unit types
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/time_entry_unit_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entry_unit_types_time_entry_unit_type_id_get(client):
    """Test case for time_entry_unit_types_time_entry_unit_type_id_get

    View time entry unit type
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/time_entry_unit_types/{time_entry_unit_type_id}'.format(time_entry_unit_type_id='time_entry_unit_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

