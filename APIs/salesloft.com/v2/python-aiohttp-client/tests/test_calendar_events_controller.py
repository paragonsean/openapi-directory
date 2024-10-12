# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calendar_event import CalendarEvent


pytestmark = pytest.mark.asyncio

async def test_v2_calendar_events_get(client):
    """Test case for v2_calendar_events_get

    List calendar events
    """
    params = [('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('start_time', 'start_time_example'),
                    ('end_time', 'end_time_example'),
                    ('user_guid', 'user_guid_example'),
                    ('calendar_id', 'calendar_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/calendar/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_calendar_events_upsert_post(client):
    """Test case for v2_calendar_events_upsert_post

    Upsert a calendar event
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'all_day': True,
        'attendees': None,
        'calendar_id': 'calendar_id_example',
        'canceled_at': 'canceled_at_example',
        'description': 'description_example',
        'end_time': '2013-10-20',
        'i_cal_uid': 'i_cal_uid_example',
        'id': 'id_example',
        'location': 'location_example',
        'organizer': 'organizer_example',
        'recurring': True,
        'start_time': '2013-10-20',
        'status': 'status_example',
        'title': 'title_example',
        'updated_at': 'updated_at_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/calendar/events/upsert',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

