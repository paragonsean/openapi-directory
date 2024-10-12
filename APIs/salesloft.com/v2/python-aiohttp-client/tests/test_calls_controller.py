# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.call import Call


pytestmark = pytest.mark.asyncio

async def test_v2_activities_calls_id_json_get(client):
    """Test case for v2_activities_calls_id_json_get

    Fetch a call
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/activities/calls/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_activities_calls_json_get(client):
    """Test case for v2_activities_calls_json_get

    List calls
    """
    params = [('ids', [56]),
                    ('created_at', ['created_at_example']),
                    ('updated_at', ['updated_at_example']),
                    ('user_guid', ['user_guid_example']),
                    ('person_id', [56]),
                    ('sentiment', ['sentiment_example']),
                    ('disposition', ['disposition_example']),
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
        path='/v2/activities/calls.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_activities_calls_json_post(client):
    """Test case for v2_activities_calls_json_post

    Create a call
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'action_id': 56,
        'crm_params': None,
        'disposition': 'disposition_example',
        'duration': 56,
        'linked_call_data_record_ids': [56],
        'notes': 'notes_example',
        'person_id': 56,
        'sentiment': 'sentiment_example',
        'to': 'to_example',
        'user_guid': 'user_guid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/activities/calls.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

