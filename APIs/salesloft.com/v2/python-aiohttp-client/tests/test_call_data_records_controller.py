# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.call_data_record import CallDataRecord


pytestmark = pytest.mark.asyncio

async def test_v2_call_data_records_id_json_get(client):
    """Test case for v2_call_data_records_id_json_get

    Fetch a call data record
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/call_data_records/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_call_data_records_json_get(client):
    """Test case for v2_call_data_records_json_get

    List call data records
    """
    params = [('ids', [56]),
                    ('has_call', True),
                    ('created_at', ['created_at_example']),
                    ('updated_at', ['updated_at_example']),
                    ('user_guid', ['user_guid_example']),
                    ('person_id', [56]),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/call_data_records.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

