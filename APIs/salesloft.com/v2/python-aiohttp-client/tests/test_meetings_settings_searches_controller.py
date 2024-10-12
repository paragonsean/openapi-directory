# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.meeting_setting import MeetingSetting


pytestmark = pytest.mark.asyncio

async def test_v2_meetings_settings_searches_json_post(client):
    """Test case for v2_meetings_settings_searches_json_post

    List meeting settings
    """
    params = [('user_guids', ['user_guids_example']),
                    ('updated_at', ['updated_at_example']),
                    ('calendar_type', 'calendar_type_example'),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/v2/meetings/settings/searches.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

