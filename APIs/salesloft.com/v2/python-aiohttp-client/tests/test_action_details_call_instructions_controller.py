# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.call_instruction import CallInstruction


pytestmark = pytest.mark.asyncio

async def test_v2_action_details_call_instructions_id_json_get(client):
    """Test case for v2_action_details_call_instructions_id_json_get

    Fetch a call instructions
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/action_details/call_instructions/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_action_details_call_instructions_json_get(client):
    """Test case for v2_action_details_call_instructions_json_get

    List call instructions
    """
    params = [('ids', [56]),
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
        path='/v2/action_details/call_instructions.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

