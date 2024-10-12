# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attendee_by_meeting import AttendeeByMeeting
from openapi_server.models.historical_meeting import HistoricalMeeting
from openapi_server.models.meeting_by_id import MeetingById
from openapi_server.models.meeting_created import MeetingCreated
from openapi_server.models.meeting_history import MeetingHistory
from openapi_server.models.meeting_req_create import MeetingReqCreate
from openapi_server.models.meeting_req_update import MeetingReqUpdate
from openapi_server.models.start_url import StartUrl
from openapi_server.models.upcoming_meeting import UpcomingMeeting


pytestmark = pytest.mark.asyncio

async def test_historical_meetings_get(client):
    """Test case for historical_meetings_get

    Get historical meetings
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/historicalMeetings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meetings_get(client):
    """Test case for meetings_get

    DEPRECATED: Get historical meetings
    """
    params = [('history', True),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/meetings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meetings_meeting_id_attendees_get(client):
    """Test case for meetings_meeting_id_attendees_get

    Get attendees by meeting
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/meetings/{meeting_id}/attendees'.format(meeting_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meetings_meeting_id_delete(client):
    """Test case for meetings_meeting_id_delete

    Delete meeting
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/G2M/rest/meetings/{meeting_id}'.format(meeting_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meetings_meeting_id_get(client):
    """Test case for meetings_meeting_id_get

    Get meeting
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/meetings/{meeting_id}'.format(meeting_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meetings_meeting_id_put(client):
    """Test case for meetings_meeting_id_put

    Update meeting
    """
    body = {"meetingtype":"immediate","subject":"subject","endtime":"2000-01-23T04:56:07.000+00:00","passwordrequired":True,"starttime":"2000-01-23T04:56:07.000+00:00","timezonekey":"timezonekey","conferencecallinfo":"conferencecallinfo"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/G2M/rest/meetings/{meeting_id}'.format(meeting_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meetings_meeting_id_start_get(client):
    """Test case for meetings_meeting_id_start_get

    Start meeting
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/meetings/{meeting_id}/start'.format(meeting_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meetings_post(client):
    """Test case for meetings_post

    Create meeting
    """
    body = {"meetingtype":"immediate","subject":"subject","endtime":"2000-01-23T04:56:07.000+00:00","passwordrequired":True,"starttime":"2000-01-23T04:56:07.000+00:00","timezonekey":"timezonekey","conferencecallinfo":"conferencecallinfo"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2M/rest/meetings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upcoming_meetings_get(client):
    """Test case for upcoming_meetings_get

    Get upcoming meetings
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/upcomingMeetings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

