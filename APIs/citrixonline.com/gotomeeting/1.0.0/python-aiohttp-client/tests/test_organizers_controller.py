# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attendee_by_organizer import AttendeeByOrganizer
from openapi_server.models.historical_meeting import HistoricalMeeting
from openapi_server.models.meeting_by_organizer import MeetingByOrganizer
from openapi_server.models.organizer import Organizer
from openapi_server.models.organizer_req import OrganizerReq
from openapi_server.models.organizer_short import OrganizerShort
from openapi_server.models.organizer_status import OrganizerStatus
from openapi_server.models.upcoming_meeting import UpcomingMeeting


pytestmark = pytest.mark.asyncio

async def test_organizers_delete(client):
    """Test case for organizers_delete

    Delete organizer by email
    """
    params = [('email', 'email_example')]
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/G2M/rest/organizers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizers_get(client):
    """Test case for organizers_get

    Get organizer by email / Get all organizers
    """
    params = [('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/organizers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizers_organizer_key_attendees_get(client):
    """Test case for organizers_organizer_key_attendees_get

    Get attendees by organizer
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/organizers/{organizer_key}/attendees'.format(organizer_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizers_organizer_key_delete(client):
    """Test case for organizers_organizer_key_delete

    Delete organizer
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/G2M/rest/organizers/{organizer_key}'.format(organizer_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizers_organizer_key_get(client):
    """Test case for organizers_organizer_key_get

    Get organizer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/organizers/{organizer_key}'.format(organizer_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizers_organizer_key_historical_meetings_get(client):
    """Test case for organizers_organizer_key_historical_meetings_get

    Get historical meetings by organizer
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/organizers/{organizer_key}/historicalMeetings'.format(organizer_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizers_organizer_key_meetings_get(client):
    """Test case for organizers_organizer_key_meetings_get

    DEPRECATED: Get meetings by organizer
    """
    params = [('scheduled', True),
                    ('history', True),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/organizers/{organizer_key}/meetings'.format(organizer_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizers_organizer_key_put(client):
    """Test case for organizers_organizer_key_put

    Update organizer
    """
    body = {"productType":"G2M","status":"suspended"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/G2M/rest/organizers/{organizer_key}'.format(organizer_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizers_organizer_key_upcoming_meetings_get(client):
    """Test case for organizers_organizer_key_upcoming_meetings_get

    Get upcoming meetings by organizer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/organizers/{organizer_key}/upcomingMeetings'.format(organizer_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizers_post(client):
    """Test case for organizers_post

    Create organizer
    """
    body = {"firstName":"firstName","lastName":"lastName","organizerEmail":"organizerEmail","productType":"G2M"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2M/rest/organizers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

