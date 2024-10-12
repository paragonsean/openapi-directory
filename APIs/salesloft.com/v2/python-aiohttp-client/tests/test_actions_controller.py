# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action import Action


pytestmark = pytest.mark.asyncio

async def test_v2_actions_id_json_get(client):
    """Test case for v2_actions_id_json_get

    Fetch an action
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/actions/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_actions_json_get(client):
    """Test case for v2_actions_json_get

    List actions
    """
    params = [('ids', [56]),
                    ('step_id', 56),
                    ('type', 'type_example'),
                    ('due_on', ['due_on_example']),
                    ('user_guid', ['user_guid_example']),
                    ('person_id', [56]),
                    ('cadence_id', [56]),
                    ('multitouch_group_id', [56]),
                    ('updated_at', ['updated_at_example']),
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
        path='/v2/actions.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

