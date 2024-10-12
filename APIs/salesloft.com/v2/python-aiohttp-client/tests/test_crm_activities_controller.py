# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.crm_activity import CrmActivity


pytestmark = pytest.mark.asyncio

async def test_v2_crm_activities_id_json_get(client):
    """Test case for v2_crm_activities_id_json_get

    Fetch a crm activity
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/crm_activities/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_crm_activities_json_get(client):
    """Test case for v2_crm_activities_json_get

    List crm activities
    """
    params = [('ids', [56]),
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
        path='/v2/crm_activities.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

