# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email_template import EmailTemplate


pytestmark = pytest.mark.asyncio

async def test_v2_email_templates_id_json_get(client):
    """Test case for v2_email_templates_id_json_get

    Fetch an email template
    """
    params = [('include_signature', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/email_templates/{id_jso}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_email_templates_json_get(client):
    """Test case for v2_email_templates_json_get

    List email templates
    """
    params = [('ids', [56]),
                    ('updated_at', ['updated_at_example']),
                    ('linked_to_team_template', True),
                    ('search', 'search_example'),
                    ('tag_ids', [56]),
                    ('tag', ['tag_example']),
                    ('filter_by_owner', True),
                    ('group_id', [56]),
                    ('include_cadence_templates', True),
                    ('include_archived_templates', True),
                    ('cadence_id', [56]),
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
        path='/v2/email_templates.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

