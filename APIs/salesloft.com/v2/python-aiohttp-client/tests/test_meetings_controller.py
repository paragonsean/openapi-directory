# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.meeting import Meeting


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_meetings_id_json_put(client):
    """Test case for v2_meetings_id_json_put

    Update a meeting
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'event_id': 'event_id_example',
        'i_cal_uid': 'i_cal_uid_example',
        'no_show': True,
        'reschedule_status': 'reschedule_status_example',
        'status': 'status_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/meetings/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_meetings_json_get(client):
    """Test case for v2_meetings_json_get

    List meetings
    """
    params = [('ids', [56]),
                    ('status', 'status_example'),
                    ('person_id', 'person_id_example'),
                    ('account_id', 'account_id_example'),
                    ('person_ids', [56]),
                    ('event_ids', ['event_ids_example']),
                    ('i_cal_uids', ['i_cal_uids_example']),
                    ('task_ids', [56]),
                    ('include_meetings_settings', True),
                    ('start_time', ['start_time_example']),
                    ('created_at', ['created_at_example']),
                    ('user_guids', ['user_guids_example']),
                    ('show_deleted', True),
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
        path='/v2/meetings.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

