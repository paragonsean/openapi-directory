# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attendee_by_group import AttendeeByGroup
from openapi_server.models.group import Group
from openapi_server.models.historical_meeting_by_group import HistoricalMeetingByGroup
from openapi_server.models.history_meeting_by_group import HistoryMeetingByGroup
from openapi_server.models.organizer_by_group import OrganizerByGroup
from openapi_server.models.organizer_req import OrganizerReq
from openapi_server.models.organizer_short import OrganizerShort
from openapi_server.models.upcoming_meeting_by_group import UpcomingMeetingByGroup


pytestmark = pytest.mark.asyncio

async def test_groups_get(client):
    """Test case for groups_get

    Get groups
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/groups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_group_key_attendees_get(client):
    """Test case for groups_group_key_attendees_get

    Get attendees by group
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/groups/{group_key}/attendees'.format(group_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_group_key_historical_meetings_get(client):
    """Test case for groups_group_key_historical_meetings_get

    Get historical meetings by group
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/groups/{group_key}/historicalMeetings'.format(group_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_group_key_meetings_get(client):
    """Test case for groups_group_key_meetings_get

    DEPRECATED: Get historical meetings by group
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
        path='/G2M/rest/groups/{group_key}/meetings'.format(group_key=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_group_key_organizers_get(client):
    """Test case for groups_group_key_organizers_get

    Get organizers by group
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/groups/{group_key}/organizers'.format(group_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_group_key_organizers_post(client):
    """Test case for groups_group_key_organizers_post

    Create organizer in group
    """
    body = {"firstName":"firstName","lastName":"lastName","organizerEmail":"organizerEmail","productType":"G2M"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/G2M/rest/groups/{group_key}/organizers'.format(group_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_group_key_upcoming_meetings_get(client):
    """Test case for groups_group_key_upcoming_meetings_get

    Get upcoming meetings by group
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/G2M/rest/groups/{group_key}/upcomingMeetings'.format(group_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

