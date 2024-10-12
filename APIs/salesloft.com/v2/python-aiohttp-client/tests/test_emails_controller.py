# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email import Email


pytestmark = pytest.mark.asyncio

async def test_v2_activities_emails_id_json_get(client):
    """Test case for v2_activities_emails_id_json_get

    Fetch an email
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/activities/emails/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_activities_emails_json_get(client):
    """Test case for v2_activities_emails_json_get

    List emails
    """
    params = [('ids', [56]),
                    ('updated_at', ['updated_at_example']),
                    ('bounced', True),
                    ('crm_activity_id', [56]),
                    ('action_id', [56]),
                    ('user_id', [56]),
                    ('status', ['status_example']),
                    ('cadence_id', [56]),
                    ('step_id', [56]),
                    ('one_off', True),
                    ('scoped_fields', ['scoped_fields_example']),
                    ('person_id', [56]),
                    ('email_addresses', ['email_addresses_example']),
                    ('personalization', ['personalization_example']),
                    ('sent_at', ['sent_at_example']),
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
        path='/v2/activities/emails.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

