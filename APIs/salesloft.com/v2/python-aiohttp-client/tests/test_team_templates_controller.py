# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.team_template import TeamTemplate


pytestmark = pytest.mark.asyncio

async def test_v2_team_templates_id_json_get(client):
    """Test case for v2_team_templates_id_json_get

    Fetch a team template
    """
    params = [('include_signature', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/team_templates/{id_jso}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_team_templates_json_get(client):
    """Test case for v2_team_templates_json_get

    List team templates
    """
    params = [('ids', ['ids_example']),
                    ('updated_at', ['updated_at_example']),
                    ('search', 'search_example'),
                    ('tag_ids', [56]),
                    ('tag', ['tag_example']),
                    ('include_archived_templates', True),
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
        path='/v2/team_templates.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

