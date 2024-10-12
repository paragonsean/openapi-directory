# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.meeting_setting import MeetingSetting


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_meetings_settings_id_json_put(client):
    """Test case for v2_meetings_settings_id_json_put

    Update a meeting setting
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'allow_booking_on_behalf': True,
        'allow_booking_overtime': True,
        'allow_event_overlap': True,
        'availability_limit': 56,
        'availability_limit_enabled': True,
        'buffer_time_duration': 56,
        'calendar_type': 'calendar_type_example',
        'default_meeting_length': 56,
        'description': 'description_example',
        'enable_calendar_sync': True,
        'enable_dynamic_location': True,
        'location': 'location_example',
        'primary_calendar_connection_failed': True,
        'primary_calendar_id': 'primary_calendar_id_example',
        'primary_calendar_name': 'primary_calendar_name_example',
        'reschedule_meetings_enabled': True,
        'schedule_buffer_enabled': True,
        'schedule_delay': 56,
        'share_event_detail': True,
        'time_zone': 'time_zone_example',
        'times_available': None,
        'title': 'title_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/meetings/settings/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

